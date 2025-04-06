import logging
from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from typing import Any, Iterable, Iterator, NamedTuple, Sequence, Type

import torch
from tdm import TalismanDocument, not_filter
from tdm.abstract.datamodel import FactStatus
from tdm.datamodel.facts import AtomValueFact, MentionFact, PropertyFact
from tdm.datamodel.mentions import TextNodeMention
from tdm.datamodel.nodes import TextNodeMetadata
from tdm.datamodel.values import StringValue
from transformers import pipeline
from typing_extensions import Self

from tie_ml_base.env import get_cpu_batch_size, get_gpu_batch_size, get_text2text_max_length
from tie_ml_base.huggingface_pipeline.normalization_wrapper.config import StringNormalizerConfig
from tie_ml_base.tools.memory_management import cuda_handler
from tie_ml_base.torch_wrapper import TorchModule
from tp_interfaces.abstract import AbstractConfigConstructableModel, AbstractDocumentProcessor
from tp_interfaces.domain.abstract import AbstractLiteralValueType
from tp_interfaces.domain.manager import DomainManager

logger = logging.getLogger(__name__)


@dataclass
class TextMentionData:
    language: str
    related_facts: list[AtomValueFact]
    text: str

    @property
    def get_request(self) -> str:
        return f">>{self.language}<< {self.text}"


_MentionData = NamedTuple('_MentionData', (('lang', str), ('text', str)))


class Text2TextNormalizer(
    TorchModule,
    AbstractConfigConstructableModel,
    AbstractDocumentProcessor[StringNormalizerConfig]
):
    """
    A hugging face pipeline wrapper for AtomValueFact's StringValue normalization using text2text model,
    for some supported languages.
    """
    def __init__(self, normalizer_pipeline: pipeline, model_languages: Iterable[str], preferred_device: str | torch.device = None):
        super().__init__(preferred_device=preferred_device)
        self._pipeline = normalizer_pipeline
        self._model = self._pipeline.model
        self._model_languages = tuple(model_languages)
        self._tokenizer = self._pipeline.tokenizer
        self._cpu_batch_size = get_cpu_batch_size()
        self._gpu_batch_size = get_gpu_batch_size()
        self._max_token_len = get_text2text_max_length() or 150
        self._possible_type_ids: set[str] | None = None

    async def __aenter__(self) -> Self:
        async with DomainManager() as manager:
            domain = await manager.domain

        self._possible_type_ids = {t.id for t in domain.get_types(AbstractLiteralValueType) if t.value_type is StringValue}
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._possible_type_ids = None

    async def process_doc(self, document: TalismanDocument, config: StringNormalizerConfig) -> TalismanDocument:
        def _filter(atom: AtomValueFact) -> bool:
            if atom.str_type_id not in self._possible_type_ids:
                return False
            if not config.possible_types or atom.str_type_id in config.possible_types:
                return True

            return any(prop.str_type_id in config.possible_types for prop in document.related_facts(atom, PropertyFact))

        facts = document.get_facts(
            type_=AtomValueFact,
            filter_=(not_filter(AtomValueFact.status_filter([FactStatus.APPROVED, FactStatus.DECLINED])),
                     AtomValueFact.empty_value_filter(), _filter)
        )
        return document.with_facts(await self.normalize_facts(list(facts), document, config))

    def _get_mention_data(self, mention_fact: MentionFact, config: StringNormalizerConfig) -> _MentionData | None:
        if not isinstance(mention_fact.mention, TextNodeMention):
            return None

        mention: TextNodeMention = mention_fact.mention
        node_language = mention.node.metadata.language or TextNodeMetadata.UNKNOWN_LANG
        lang = config.lang_strategy.get_lang(node_language, self._model_languages)
        if lang not in self._model_languages:
            logger.warning(f'Ignore mention <{mention_fact.id}> because unsupported language <{lang}>. '
                           f'Supported languages: {", ".join(self._model_languages)}')
            return None

        mention_len = mention.end - mention.start
        if mention_len > self._max_token_len:
            logger.warning(f'Ignore mention <{mention_fact.id}> because length of mention <{mention_len}> nore than max length <'
                           f'{self._max_token_len}>.')
            return None
        text = mention.node.content[mention.start: mention.end]
        return _MentionData(lang=lang, text=text)

    def _collect_mention_data(self, mentions: Iterator[MentionFact], config: StringNormalizerConfig) -> Sequence[TextMentionData]:
        res: dict[_MentionData, list[AtomValueFact]] = defaultdict(list)

        for mention in mentions:
            lang_text = self._get_mention_data(mention, config)
            if lang_text:
                res[lang_text].append(mention.value)

        return [TextMentionData(language=data.lang, related_facts=values, text=data.text) for data, values in res.items()]

    async def normalize_facts(self, facts: Iterable[AtomValueFact], doc: TalismanDocument, config: StringNormalizerConfig)\
            -> Iterable[AtomValueFact]:
        possible_mentions = (m for atom in facts for m in doc.related_facts(atom, type_=MentionFact))
        mentions = self._collect_mention_data(possible_mentions, config)
        normalized_mentions = self._normalize_mentions(mentions)

        fact_values = defaultdict(list)
        for normalized_mention in normalized_mentions:
            for fact in normalized_mention.related_facts:
                fact_values[fact].extend(self._convert(normalized_mention.text))

        return [replace(fact, value=tuple(self._set_confidence(fact_values[fact]))) if fact in fact_values else fact for fact in facts]

    async def normalize_fact(self, fact: AtomValueFact, doc: TalismanDocument, config: StringNormalizerConfig) -> AtomValueFact:
        res = tuple(await self.normalize_facts([fact], doc, config))
        return res[0] if len(res) else fact

    @cuda_handler
    def _normalize_mentions(self, mentions: Sequence[TextMentionData]) -> Sequence[TextMentionData]:
        if not mentions:
            return []
        # Normalization part
        self._pipeline.device = self.device
        batch_size = self._cpu_batch_size if self.device == torch.device('cpu') else self._gpu_batch_size
        to_be_normalized = [mention.get_request for mention in mentions]
        # Setting the maximum output tokens' number to (1.5 * maximum input tokens' number) to prevent value cutting.
        max_output_tokens = int(1.5 * len(max(map(self._tokenizer.encode, to_be_normalized), key=len)))
        try:
            results = self._pipeline(to_be_normalized, clean_up_tokenization_spaces=True, num_beams=5,
                                     batch_size=batch_size, max_new_tokens=max_output_tokens)
            logger.info(f'Normalize mentions: {to_be_normalized}')
        except ValueError:
            logger.warning(f'ValueError occurred during normalization of mentions: {", ".join([m.text for m in mentions])}.')
            return []

        return [replace(mention, text=result['generated_text']) for mention, result in zip(mentions, results)]

    @staticmethod
    def _convert(value: str) -> Iterator[StringValue]:
        try:
            yield StringValue(value=value)
        except ValueError:
            logger.warning(f'ValueError occurred during conversion of "{value}".')

    @staticmethod
    def _set_confidence(normalized_mentions: Iterable[StringValue]) -> Iterator[StringValue]:
        """
        Counts the confidence for each normalized value and sorts the values by confidence.
        """
        c = Counter(normalized_mentions)
        for value, value_count in c.most_common():
            yield replace(value, confidence=value_count / c.total())

    def forward(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @classmethod
    def from_config(cls, config: dict) -> Self:
        return cls.from_model_name(**config)

    @classmethod
    def from_model_name(cls, model_name_or_path: str, model_languages: Iterable[str], preferred_device: str | torch.device = None) -> Self:
        pl = pipeline(
            model=model_name_or_path,
            tokenizer=model_name_or_path,
            task='text2text-generation',
            framework='pt',
            device=torch.device('cpu')
        )
        return cls(pl, model_languages, preferred_device)

    @property
    def config_type(self) -> Type[StringNormalizerConfig]:
        return StringNormalizerConfig
