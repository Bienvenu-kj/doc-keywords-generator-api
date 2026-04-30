from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

from .application.dto.corpus_response import CorpusResponse
from .Domain.services.preprocessors.cleaner import CleanerService
from .Domain.services.preprocessors.normalizer import NormalizerService
from .Domain.services.preprocessors.tokenizer import TokenizerService
from .application.dto.keyword_request import KeywordGenerationRequest
from .infrastructure.prepocessors_adapters.native.native_cleaner import InMemoryNativeCleaner
from .infrastructure.prepocessors_adapters.native.native_normalizer import InMemoryNativeNormalizer
from .infrastructure.prepocessors_adapters.native.native_tokenizer import InMemoryNativeTokenizer
from .application.dto.keyword_response import KeywordGenerationResponse
from .application.use_cases.build_corpus import BuildCorpusUseCase
from .application.use_cases.generate_keywords import GenerateKeywordsUseCase
from .Domain.models.corpus import Corpus
from .Domain.services.data_accessors.corpus_service import CorpusService
from .Domain.services.preprocessors.term_constructor import TermConstructorService
from .infrastructure.database.file_system_adapters.fs_corpus_repository import (
    FileSystemCorpusRepository,
)
from .infrastructure.utils.custom_print import print_c


corpus_service = CorpusService(
    corpus_repository=FileSystemCorpusRepository(),
    term_constructor= TermConstructorService(),
    cleaner=CleanerService(cleaner=InMemoryNativeCleaner()),
    tokenizer=TokenizerService(tokenizer=InMemoryNativeTokenizer()),
    normalizer=NormalizerService(normalizer=InMemoryNativeNormalizer()),
)
build_corpus_use_case = BuildCorpusUseCase(corpus_service)
generate_keywords_use_case = GenerateKeywordsUseCase()
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
    global corpus_service, build_corpus_use_case, generate_keywords_use_case, corpus

    print_c("success", "Starting lifespan")
    print_c("success", "Initialisation du corpus en cours...")

    corpus_service = CorpusService(
       corpus_repository= FileSystemCorpusRepository(),
        term_constructor= TermConstructorService(),
        cleaner=CleanerService(cleaner=InMemoryNativeCleaner()),
        tokenizer=TokenizerService(tokenizer=InMemoryNativeTokenizer()),
        normalizer=NormalizerService(normalizer=InMemoryNativeNormalizer()),
    )
    build_corpus_use_case = BuildCorpusUseCase(corpus_service)
    generate_keywords_use_case = GenerateKeywordsUseCase()
    corpus = await build_corpus_use_case.execute(DEFAULT_ASSETS_PATH.as_posix())

    print_c("success", "--------------------------------------")
    print_c("success", "Initialisation du corpus terminée")

    yield
    print_c("success", "--------------------------------------")
    print_c("success", "Ending lifespan")


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
    print_c("success", "La requette pour générer les mots-clés est bien reçue")
    corpus = (await corpus_service.construct_corpus(DEFAULT_ASSETS_PATH.as_posix())) if corpus is None else corpus
    return await generate_keywords_use_case.execute(data=data,corpus=corpus)
