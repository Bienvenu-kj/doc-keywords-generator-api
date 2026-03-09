from pathlib import Path
from src.utils.readers import reader

documentsPath = Path("src/assets");



def getCorpus():
    documents = list(documentsPath.glob("*.pdf"))
    for document in documents:
        reader(document_path=document)
    return documents[:4]  # Return only the first 5 documents


if __name__ == "__main__":
    getCorpus()