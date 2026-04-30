from typing import Annotated

from fastapi import  Form

from ...Domain.models.document import Document
from ...Domain.services.keywords_generator.keywords_generator_service import KeywordsGeneratorService
from ...Domain.services.preprocessors.cleaner import CleanerService
from ...Domain.services.preprocessors.normalizer import NormalizerService
from ...Domain.services.preprocessors.term_constructor import TermConstructorService
from ...Domain.services.preprocessors.tokenizer import TokenizerService
from ...infrastructure.prepocessors_adapters.native.native_cleaner import InMemoryNativeCleaner
from ...infrastructure.prepocessors_adapters.native.native_normalizer import InMemoryNativeNormalizer
from ...infrastructure.prepocessors_adapters.native.native_tokenizer import InMemoryNativeTokenizer
from ...infrastructure.utils.document_content_preparators.pymupdf_prepare_document_content import pymupdf_get_document_content
from ...infrastructure.utils.readers.pymupdf_readers import PymupdfReader
from ...infrastructure.utils.custom_print import print_c
from ..dto.keyword_request import KeywordGenerationRequest
from ...Domain.models.corpus import Corpus
from ..dto.keyword_response import KeywordGenerationResponse


class GenerateKeywordsUseCase:
    @staticmethod
    async def execute(data: Annotated[KeywordGenerationRequest, Form(media_type="multipart/form-data")],corpus:Corpus|None) -> KeywordGenerationResponse:
        if corpus is None:
            print_c("error","Le corpus est vide")

        print_c("success","La requette reçue: On commence la génération des keywords...")

        # contenu brut du document
        document_content = await pymupdf_get_document_content(await PymupdfReader(uploaded_document=data.file).read())

        """
        Prétraitement du document
        """
        # normalisation
        normalized_content = await NormalizerService(normalizer=InMemoryNativeNormalizer()).normalize(document_content)

        # nettoyage
        cleaned_content = await CleanerService(cleaner=InMemoryNativeCleaner()).clean(normalized_content)

        # tokenisation
        tokens = await TokenizerService(tokenizer=InMemoryNativeTokenizer()).tokenize(cleaned_content,n_gram=False)

        # construction de terms avec 0 comme valeur aux propriétés tf, idf et tf_idf
        terms = await TermConstructorService().construct_terms(tokens)

        document = Document(
            name=str(data.file.filename),
            path="",
            content="",
            all_terms=tokens,
            all_unique_terms=terms,
            doc_type=str(data.file.filename.split(".")[1]),
        )

        keywords = await KeywordsGeneratorService(corpus=corpus, max_keywords_count=data.max_keywords_count, document=document).generate_keywords()

        print_c("success","génération terminée : Félicitation !")
        # En attendant le vrai pipeline TF-IDF, on conserve une réponse de demonstration.
        return KeywordGenerationResponse(
            document_name=str(data.file.filename),
            success=True,
             keywords=keywords
             # [
            #     Keyword(
            #         term=Term(
            #             name="intelligence artificielle",
            #             is_n_gram=True,
            #             tf_score=0.45,
            #             idf_score=0.5,
            #             tf_idf_score=0.95,
            #         )
            #     ),
            #     Keyword(
            #         term=Term(
            #             name="Python",
            #             is_n_gram=True,
            #             tf_score=0.5,
            #             idf_score=0.5,
            #             tf_idf_score=0.87,
            #         )
            #     ),
            #     Keyword(
            #         term=Term(
            #             name="APIe",
            #             is_n_gram=True,
            #             tf_score=0.5,
            #             idf_score=0.5,
            #             tf_idf_score=0.78,
            #         )
            #     ),
            # ]
        )
