from abc import ABC, abstractmethod

from ..models.document import Document
from ..models.term import Term


class TFProcessor(ABC):
    @abstractmethod
    def tf_processing(self, document: Document, term_name) -> Term:
        pass
