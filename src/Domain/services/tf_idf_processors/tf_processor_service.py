from Domain.models.document import Document
from Domain.models.term import Term
from Domain.ports.tf_idf_processors.i_tf_processor import TFProcessor


class TFProcessorService:
    def __init__(self, tf_processor:TFProcessor):
        self.tf_processor = tf_processor

    async def process(self, document: Document, term_name:str) -> Term:
        return await self.tf_processor.tf_processing(document=document, term_name=term_name)