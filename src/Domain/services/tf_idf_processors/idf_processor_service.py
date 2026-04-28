from Domain.models.corpus import Corpus
from Domain.models.term import Term
from Domain.ports.tf_idf_processors.i_idf_processor import IDFProcessor


class IDFProcessorService:
    def __init__(self, idf_processor:IDFProcessor):
        self.idf_processor = idf_processor

    async def idf_processing(self, corpus: Corpus, term_name:str) -> Term:
        return await self.idf_processor.process(corpus=corpus, term_name=term_name)