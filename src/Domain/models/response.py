from pydantic import BaseModel
from typing import List
from .keyword import Keyword


class KeywordsApiResponse(BaseModel):
    success: bool
    document_name: str
    keywords: List[Keyword]
