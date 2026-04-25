from abc import ABC, abstractmethod

from ..models.corpus import Corpus
from ..models.term import Term


class IDFProcessor(ABC):
    @abstractmethod
    def process(self, corpus: Corpus, term_name) -> Term:
        pass