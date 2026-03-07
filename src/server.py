from fastapi import FastAPI, UploadFile
from src.models.pydanc import KeywordsApiResponse, KeywordApiResponse

app = FastAPI()

@app.get("/")
def root():
    return "Salut"

@app.post("/keywords")
def keywordsGenerating(document: UploadFile):
    # Exemple de réponse avec des mots-clés fictifs
    sample_keywords = [
        KeywordApiResponse(term="intelligence artificielle", score=0.95),
        KeywordApiResponse(term="génération de mots-clés", score=0.87),
        KeywordApiResponse(term="API", score=0.78)
    ]
    response = KeywordsApiResponse(document_name=document.filename, keywords=sample_keywords)
    return response 