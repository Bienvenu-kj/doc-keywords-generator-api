from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

from .application.dto.corpus_response import CorpusResponse
from .application.dto.keyword_request import KeywordGenerationRequest
from .application.dto.keyword_response import KeywordGenerationResponse
from .application.use_cases.build_corpus import BuildCorpusUseCase
from .application.use_cases.generate_keywords import GenerateKeywordsUseCase
from .Domain.models.corpus import Corpus
from .Domain.ports.custom_print import CustomPrintData
from .Domain.services.data_accessors.corpus_service import CorpusService
from .Domain.services.preprocessors.term_constructor import TermConstructorService
from .infrastructure.utils.document_content_preparators.pymupdf_prepare_document_content import InMemoryPymuPDFDocumentContentExtractor
from .infrastructure.prepocessors_adapters.native.native_cleaner import InMemoryNativeCleaner
from .infrastructure.prepocessors_adapters.native.native_normalizer import InMemoryNativeNormalizer
from .infrastructure.prepocessors_adapters.native.native_tokenizer import InMemoryNativeTokenizer
from .infrastructure.utils.custom_printers.colorama_custom_printer import ColoramaCustomPrinter
from .infrastructure.database.file_system_adapters.fs_corpus_repository import (
    FileSystemCorpusRepository,
)



corpus_service = CorpusService(
    corpus_repository=FileSystemCorpusRepository(),
    term_constructor= TermConstructorService(),
    cleaner=InMemoryNativeCleaner(),
    tokenizer=InMemoryNativeTokenizer(),
    normalizer=InMemoryNativeNormalizer(),
    custom_printer=ColoramaCustomPrinter(),
)
build_corpus_use_case = BuildCorpusUseCase(corpus_service)
corpus: Corpus | None = None
DEFAULT_ASSETS_PATH = (
    Path(__file__).resolve().parent
    / "infrastructure"
    / "database"
    / "file_system_adapters"
    / "assets"
)


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    global corpus_service, build_corpus_use_case, corpus

    ColoramaCustomPrinter().print(CustomPrintData("success", "Starting lifespan"))
    ColoramaCustomPrinter().print(CustomPrintData("success", "Initialisation du corpus en cours..."))

    corpus_service = CorpusService(
       corpus_repository= FileSystemCorpusRepository(),
        term_constructor= TermConstructorService(),
        cleaner=InMemoryNativeCleaner(),
        tokenizer=InMemoryNativeTokenizer(),
        normalizer=InMemoryNativeNormalizer(),
        custom_printer=ColoramaCustomPrinter(),
    )
    build_corpus_use_case = BuildCorpusUseCase(corpus_service)
    corpus = await build_corpus_use_case.execute(DEFAULT_ASSETS_PATH.as_posix())

    ColoramaCustomPrinter().print(CustomPrintData("success", "--------------------------------------"))
    ColoramaCustomPrinter().print(CustomPrintData("success", "Initialisation du corpus terminée"))

    yield
    ColoramaCustomPrinter().print(CustomPrintData("success", "--------------------------------------"))
    ColoramaCustomPrinter().print(CustomPrintData("success", "Ending lifespan"))


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,  # doc_type: ignore
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "Salut"


@app.get("/corpus")
async def get_corpus() -> CorpusResponse:
    # Sécurise l'endpoint même si le lifespan n'a pas été déclenché.
    if not (await corpus_service.get_corpus()).documents:
        return CorpusResponse(documents=(await corpus_service.construct_corpus(DEFAULT_ASSETS_PATH.as_posix())).documents)
    return CorpusResponse(documents=(await corpus_service.get_corpus()).documents)


@app.post("/keywords")
async def keywords_generating(data:Annotated[KeywordGenerationRequest, Form(media_type="multipart/form-data")]) -> KeywordGenerationResponse:
    global corpus_service,corpus, DEFAULT_ASSETS_PATH
    ColoramaCustomPrinter().print(CustomPrintData("success", "La requette pour générer les mots-clés est bien reçue"))
    corpus = (await corpus_service.construct_corpus(DEFAULT_ASSETS_PATH.as_posix())) if corpus is None else corpus
    return await GenerateKeywordsUseCase(normalizer=InMemoryNativeNormalizer(),cleaner=InMemoryNativeCleaner(),tokenizer=InMemoryNativeTokenizer(),document_content_extractor=InMemoryPymuPDFDocumentContentExtractor(),printer=ColoramaCustomPrinter()).execute(data=data,corpus=corpus)
