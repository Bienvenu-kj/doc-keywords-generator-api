from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from src.models.pydantic.model import KeywordsApiResponse, KeywordApiResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return "Salut"

@app.post("/keywords")
def keywordsGenerating(file: UploadFile):
    # Exemple de réponse avec des mots-clés fictifs
    sample_keywords = [
        KeywordApiResponse(term="intelligence artificielle", score=0.95),
        KeywordApiResponse(term="génération de mots-clés", score=0.87),
        KeywordApiResponse(term="API", score=0.78)
    ]
    response = KeywordsApiResponse(document_name=file.filename, keywords=sample_keywords)
    return response 