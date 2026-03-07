
from pydantic import BaseModel
from typing import List


class KeywordApiResponse(BaseModel):
    term: str
    score: float


class KeywordsApiResponse(BaseModel):
    document_name: str
    keywords: List[KeywordApiResponse]
              
