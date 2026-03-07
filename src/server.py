from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Salut"


app.post("/keywords")
def keywordsGenerating():
    return "Successful!"