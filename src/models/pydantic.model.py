
from pydantic import BaseModel
from typing import List


class KeywordApiResponse(BaseModel):
    term: str
    score: float


class KeywordsApiResponse(BaseModel):
    document_name: str
    keywords: List[KeywordApiResponse]
              

class Corpus(BaseModel):
    documents: List[str]
    all_terms: List[str]
    terms_by_document: List[List[str]]