from ..models.corpus import Corpus
from ..models.term import Term
from ..ports.idf_processor import IDFProcessor


class IDFProcessorService:
    def __init__(self, idf_processor:IDFProcessor):
        self.idf_processor = idf_processor

    def idf_processing(self, corpus: Corpus, term_name:str) -> Term:
        return self.idf_processor.process(corpus=corpus, term_name=term_name)