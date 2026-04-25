from ..models.corpus import Corpus
from ..models.term import Term
from ..ports.tf_idf_processor import TFIDFProcessor


class TFIDFProcessorService:
    def __init__(self, tf_idf_processor:TFIDFProcessor):
        self.tf_idf_processor = tf_idf_processor

    def process(self, term: Term, idf_score:float, tf_score:float) -> Term:
        return self.tf_idf_processor.process(term=term, idf_score=idf_score, tf_core=tf_score)