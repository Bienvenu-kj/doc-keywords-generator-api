from ...models.corpus import Corpus
from ...models.document import Document
from ...ports.preprocessors.i_cleaner import Cleaner
from ...ports.preprocessors.i_normalizer import Normalizer
from ...ports.preprocessors.i_tokenizer import Tokenizer
from ...ports.repositories.i_corpus_repository import CorpusRepository
from ..preprocessors.term_constructor import TermConstructorService


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

            # on normalise le contenu du document
            normalized_content = await self.normalizer.normalize(document_content)

            # nous nettoyons le contenu
            cleaned_content = await self.cleaner.clean(normalized_content)

            # on tokenise pour obtenir tous les terms, mais en version simple(str) unique ou n_gram.
            all_terms = await self.tokenizer.tokenize(cleaned_content,False)

            # on obtient les terms uniques du document, mais cette fois en version enrichie (Term).
            all_unique_terms = await self.term_constructor.construct_terms(all_terms)

            # on ajoute tous les terms obtenus
            document.__setitem__("all_terms",all_terms)

            # on ajoute tous les terms enrichis obtenus
            enriched_document = document.__setitem__("all_unique_terms",all_unique_terms)
            enriched_documents.append(
                enriched_document
            )

        self.corpus = Corpus(documents=enriched_documents)
        return self.corpus

