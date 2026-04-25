from abc import abstractmethod, ABC
from ..models.corpus import Corpus


class CorpusRepository(ABC):
    @abstractmethod
    def get_corpus(self) -> Corpus:
        pass

    @abstractmethod
    def construct_corpus(self) -> Corpus:
        pass

