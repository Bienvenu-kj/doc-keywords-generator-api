from abc import ABC, abstractmethod

from ..models.term import Term


class TFIDFProcessor(ABC):
    @abstractmethod
    def process(self,term:Term, idf_score:float, tf_core:float)->Term:
        pass