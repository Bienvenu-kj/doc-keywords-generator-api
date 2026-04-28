from ...models.corpus import Corpus
from ...models.document import Document
from ...ports.preprocessors.i_cleaner import Cleaner
from ...ports.preprocessors.i_normalizer import Normalizer
from ...ports.preprocessors.i_tokenizer import Tokenizer
from ...ports.repositories.i_corpus_repository import CorpusRepository
from ..preprocessing.term_constructor import TermConstructorService


class CorpusService:
    def __init__(
        self,
        corpus_repository: CorpusRepository,
        cleaner: Cleaner,
        normalizer: Normalizer,
        tokenizer: Tokenizer,
        term_constructor: TermConstructorService,
    ):
        self.corpus_repository = corpus_repository
        self.term_constructor = term_constructor
        self.corpus = Corpus(documents=[])
        self.cleaner = cleaner
        self.normalizer = normalizer
        self.tokenizer = tokenizer

    async def get_corpus(self) -> Corpus:
        return self.corpus

    async def construct_corpus(self, path_of_documents:str) -> Corpus:
        documents = await self.corpus_repository.load_documents(path_of_documents)
        enriched_documents: list[Document] = []

        for document in documents:
            document_content = document.content
            normalized_content = await self.normalizer.normalize(document_content)
            cleaned_content = await self.cleaner.clean(normalized_content)
            all_terms = await self.tokenizer.tokenize(cleaned_content,False)
            all_unique_terms = await self.term_constructor.construct_terms(all_terms)

            enriched_document = document.__setitem__("all_unique_terms",all_unique_terms)
            enriched_documents.append(
                enriched_document
            )

        self.corpus = Corpus(documents=enriched_documents)
        return self.corpus

