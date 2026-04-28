from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .application.dto.keyword_response import KeywordGenerationResponse
from .application.use_cases.build_corpus import BuildCorpusUseCase
from .application.use_cases.generate_keywords import GenerateKeywordsUseCase
from .Domain.models.corpus import Corpus
from .Domain.services.data_accessors.corpus_service import CorpusService
from .Domain.services.preprocessing.term_constructor import TermConstructorService
from .infrastructure.database.file_system_adapters.fs_corpus_repository import (
    FileSystemCorpusRepository,
)
from .infrastructure.utils.custom_print import print_c


corpus_service = CorpusService(
    FileSystemCorpusRepository(),
    TermConstructorService(),
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
async def lifespan(app: FastAPI):
    global corpus_service, build_corpus_use_case, generate_keywords_use_case, corpus

    print_c("success", "Initialisation du corpus")
    corpus_service = CorpusService(
        FileSystemCorpusRepository(),
        TermConstructorService(),
    )
    build_corpus_use_case = BuildCorpusUseCase(corpus_service)
    generate_keywords_use_case = GenerateKeywordsUseCase()
    corpus = await build_corpus_use_case.execute(DEFAULT_ASSETS_PATH)

    yield
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
async def get_corpus() -> Corpus:
    # Sécurise l'endpoint même si le lifespan n'a pas été déclenché.
    if not (await corpus_service.get_corpus()).documents:
        await build_corpus_use_case.execute(DEFAULT_ASSETS_PATH)
    return await corpus_service.get_corpus()


@app.post("/keywords")
async def keywords_generating(file: UploadFile) -> KeywordGenerationResponse:
    return await generate_keywords_use_case.execute(str(file.filename))
