from typing import Annotated

from fastapi import  Form

from ...Domain.ports.custom_print import CustomPrint, CustomPrintData
from ...Domain.utils.custom_print_util import CustomPrintUtil
from ...Domain.services.document_content_extractor_service import DocumentContentExtractorService
from ...Domain.ports.document_content_extractor import DocumentContentExtractor, DocumentSource
from ...Domain.ports.preprocessors.i_cleaner import Cleaner
from ...Domain.ports.preprocessors.i_normalizer import Normalizer
from ...Domain.ports.preprocessors.i_tokenizer import Tokenizer
from ...Domain.services.preprocessors.preprocessor_service import PreprocessorService
from ...Domain.models.document import Document
from ...Domain.services.keywords_generator.keywords_generator_service import KeywordsGeneratorService
from ...Domain.models.corpus import Corpus
from ..dto.keyword_response import KeywordGenerationResponse
from ..dto.keyword_request import KeywordGenerationRequest


class GenerateKeywordsUseCase:
    def __init__(self, normalizer: Normalizer, tokenizer: Tokenizer, cleaner:Cleaner, document_content_extractor: DocumentContentExtractor,printer:CustomPrint):
        self.normalizer = normalizer
        self.tokenizer = tokenizer
        self.cleaner = cleaner
        self.document_content_extractor = document_content_extractor
        self.printer = printer

    async def execute(self, data: Annotated[KeywordGenerationRequest, Form(media_type="multipart/form-data")],corpus:Corpus|None) -> KeywordGenerationResponse:
        if corpus is None:
            CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("error","Le corpus est vide")).print()

        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("warning","on commence la génération des keywords...")).print()
        document_bytes_content = await data.file.read()
        document_source_data = DocumentSource(content=document_bytes_content,document_type=str((data.file.filename or '').split(".")[-1]), name=(data.file.filename or ''))

        # contenu brut du document
        document_content = await DocumentContentExtractorService(document_content_extractor=self.document_content_extractor).extract(document_source_data)
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", "Nous avons déjà le contenu brut du document à traiter")).print()

        """
        Prétraitement du document
        """
        processing_result = await PreprocessorService(normalizer=self.normalizer,cleaner=self.cleaner,tokenizer=self.tokenizer,printer=self.printer).preprocess(document_content)

        document = Document(
            name=str(data.file.filename),
            path="",
            content="",
            all_terms=processing_result.all_terms,
            all_unique_terms=processing_result.all_unique_terms,
            doc_type=str((data.file.filename or '').split(".")[-1]),
        )

        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("warning","génération proprément-dite des mot-clés...")).print()
        keywords = await KeywordsGeneratorService(corpus=corpus, max_keywords_count=data.max_keywords_count, document=document, custom_printer=self.printer).generate_keywords()

        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success","génération des mots-clés terminée : Félicitation !")).print()

        # retourne les mots-clés générés
        return KeywordGenerationResponse(
            document_name=str(data.file.filename),
            success=True,
             keywords=keywords
        )
