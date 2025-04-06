from abc import ABCMeta, abstractmethod

from pydantic import PrivateAttr

from tp_interfaces.abstract import ImmutableBaseModel


class AbstractLanguageStrategy(ImmutableBaseModel, metaclass=ABCMeta):
    @abstractmethod
    def get_lang(self, lang: str, supported_langs: tuple[str, ...]) -> str | None:
        raise NotImplementedError


class BaseLanguageStrategy(AbstractLanguageStrategy):
    """Use node language"""

    def get_lang(self, lang: str, supported_langs: tuple[str, ...]) -> str | None:
        return lang


class ForceOneLang(AbstractLanguageStrategy):
    """
    Force language 'lang'
    if 'for_all=true' than ignore node language else use force lang only for unsupported languages
    """
    lang: str
    for_all: bool = False

    def get_lang(self, lang: str, supported_langs: tuple[str, ...]) -> str | None:
        if self.for_all:
            return self.lang

        return lang if lang in supported_langs else self.lang


class LangMappingStrategy(AbstractLanguageStrategy):
    """
    map supported language(including unknown) to list of unsupported language
    """
    lang_mapping: dict[str, tuple[str, ...]]
    _lang_mapping: dict[str, str] = PrivateAttr()  # mapping unsupported language to supported

    def __init__(self, lang_mapping: dict[str, tuple[str, ...]]):
        super().__init__(lang_mapping=lang_mapping)
        real_mapping = {value: key for key, values in self.lang_mapping.items() for value in values}
        self._lang_mapping = real_mapping

    def get_lang(self, lang: str, supported_langs: tuple[str, ...]) -> str:
        return self._lang_mapping.get(lang, lang)

    def __hash__(self):
        return hash(tuple(self.lang_mapping.items()))


class StringNormalizerConfig(ImmutableBaseModel):
    possible_types: tuple[str, ...] | None = None
    lang_strategy: BaseLanguageStrategy | ForceOneLang | LangMappingStrategy = BaseLanguageStrategy()
