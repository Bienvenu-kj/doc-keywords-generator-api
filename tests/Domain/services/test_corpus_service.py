from pathlib import Path

import pytest,re

from Domain.ports.preprocessors.i_cleaner import Cleaner
from Domain.ports.preprocessors.i_normalizer import Normalizer
from Domain.ports.preprocessors.i_tokenizer import Tokenizer
from src.Domain.models.document import Document
from src.Domain.ports.repositories.i_corpus_repository import CorpusRepository
from src.Domain.services.data_accessors.corpus_service import CorpusService
from src.Domain.services.preprocessors.term_constructor import TermConstructorService


class InMemoryCorpusRepository(CorpusRepository):
    def __init__(self, documents: list[Document]):
        self.documents = documents

    async def load_documents(self, documents_path: Path) -> list[Document]:
        return self.documents


class InMemoryCleaner(Cleaner):
    async def clean(self, content:str) -> str:
        return re.sub(
             pattern=r"[0-9+><]",
             repl="",
             string=(
                 content
                 .replace("\n", " ")
                 .replace("\t", " ")
                 .replace("\r", " ")
             ))

class InMemoryNormalizer(Normalizer):
    async def normalize(self, content:str) -> str:
        return content.lower()

class InMemoryTokenizer(Tokenizer):
    async def tokenize(self,content:str, ng_gram:bool) -> list[str]:
        return [
            term.strip()
            for term in content.split(" ")
            if term.strip()
        ]

@pytest.mark.asyncio
async def test_construct_corpus_extracts_unique_terms_from_loaded_documents():
    repository = InMemoryCorpusRepository(
        documents=[
            Document(
                name="sample.pdf",
                path="sample.pdf",
                doc_type="pdf",
                content="Python python API 101\nAPI",
                all_unique_terms=[],
                all_terms=[]
            )
        ]
    )
    service = CorpusService(corpus_repository=repository,term_constructor=TermConstructorService(), tokenizer=InMemoryTokenizer(),normalizer=InMemoryNormalizer(),cleaner=InMemoryCleaner())

    corpus = await service.construct_corpus("unused")

    assert len(corpus.documents) == 1
    assert [term.name for term in corpus.documents[0].all_unique_terms] == ["api", "python"]


@pytest.mark.asyncio
async def test_get_corpus_returns_last_constructed_corpus():
    repository = InMemoryCorpusRepository(documents=[])
    service = CorpusService(corpus_repository=repository,term_constructor=TermConstructorService(), tokenizer=InMemoryTokenizer(),normalizer=InMemoryNormalizer(),cleaner=InMemoryCleaner())

    await service.construct_corpus("")

    corpus = await service.get_corpus()

    assert corpus.documents == []
