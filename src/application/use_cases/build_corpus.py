from ...Domain.models.corpus import Corpus
from ...Domain.services.data_accessors.corpus_service import CorpusService


class BuildCorpusUseCase:
    def __init__(self, corpus_service: CorpusService):
        self.corpus_service = corpus_service

    async def execute(self, documents_path: str) -> Corpus:
        return await self.corpus_service.construct_corpus(documents_path)
