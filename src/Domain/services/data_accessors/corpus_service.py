from ...models.document import Document
from ...models.corpus import Corpus
from ...ports.custom_print import CustomPrint
from ...ports.preprocessors.i_cleaner import Cleaner
from ...ports.preprocessors.i_normalizer import Normalizer
from ...ports.preprocessors.i_tokenizer import Tokenizer
from ...ports.repositories.i_corpus_repository import CorpusRepository
from ..preprocessors.preprocessor_service import PreprocessorService
from ..preprocessors.term_constructor import TermConstructorService



class CorpusService:
    def __init__(
        self,
        corpus_repository: CorpusRepository,
        cleaner: Cleaner,
        normalizer: Normalizer,
        tokenizer: Tokenizer,
        term_constructor: TermConstructorService,
        custom_printer: CustomPrint
    ):
        self.corpus_repository = corpus_repository
        self.term_constructor = term_constructor
        self.corpus = Corpus(documents=[])
        self.cleaner = cleaner
        self.normalizer = normalizer
        self.tokenizer = tokenizer
        self.printer = custom_printer

    async def get_corpus(self) -> Corpus:
        return self.corpus

    async def construct_corpus(self, path_of_documents:str) -> Corpus:
        documents = await self.corpus_repository.load_documents(path_of_documents)
        enriched_documents: list[Document] = []

        for document in documents:
            document_content = document.content

            """
                Prétraitement du document
            """
            processing_result = await PreprocessorService(tokenizer=self.tokenizer,normalizer=self.normalizer,cleaner=self.cleaner,printer=self.printer).preprocess(document_content=document_content)


            all_terms = processing_result.all_terms
            all_unique_terms =processing_result.all_unique_terms

            # on ajoute tous les terms obtenus
            document.__setitem__("all_terms",all_terms)

            # on supprime tout le contenu, car il ne sert plus à rien dans le corpus, nous avons tous les terms qui forment le contenu
            document.__setitem__("content","")

            # on ajoute tous les terms enrichis obtenus
            enriched_document = document.__setitem__("all_unique_terms",all_unique_terms)
            enriched_documents.append(
                enriched_document
            )

        self.corpus = Corpus(documents=enriched_documents)
        return self.corpus

