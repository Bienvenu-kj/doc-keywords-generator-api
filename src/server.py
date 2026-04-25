from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from Domain.models.response import KeywordsApiResponse
from Domain.models.keyword import Keyword
from Domain.models.term import Term

app = FastAPI()

app.add_middleware(
    CORSMiddleware, #type: ignore
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return "Salut"


@app.post("/keywords")
def keywords_generating(file: UploadFile) -> KeywordsApiResponse:

    # Exemple de réponse avec des mots-clés fictifs
    sample_keywords = KeywordsApiResponse(
        success=True,
        document_name=str(file.filename),
        keywords=[
            Keyword(term=Term(isN_gram=True, name="intelligence artificielle", TFscore=0.45, IDFscore=0.5,
                              TF_IDF_Score=0.95)),
            Keyword(term=Term(isN_gram=True, name="Python", TFscore=0.5, IDFscore=0.5, TF_IDF_Score=0.87)),
            Keyword(term=Term(isN_gram=True, name="APIe", TFscore=0.5, IDFscore=0.5, TF_IDF_Score=0.78)),
        ]
    )

    response = sample_keywords
    return response
