from Domain.models.term import Term
from Domain.ports.tf_idf_processors.i_tf_idf_processor import TFIDFProcessor


class TFIDFProcessorService:
    def __init__(self, tf_idf_processor:TFIDFProcessor):
        self.tf_idf_processor = tf_idf_processor

    async def process(self, term: Term, idf_score:float, tf_score:float) -> Term:
        return await self.tf_idf_processor.process(term=term, idf_score=idf_score, tf_core=tf_score)