from ..models.document import Document
from ..models.term import Term
from ..ports.tf_processor import TFProcessor


class TFProcessorService:
    def __init__(self, tf_processor:TFProcessor):
        self.tf_processor = tf_processor

    def process(self, document: Document, term_name:str) -> Term:
        return self.tf_processor.tf_processing(document=document, term_name=term_name)