from typing import List

from pydantic import BaseModel

from ...Domain.models.keyword import Keyword





class KeywordTermResponse(BaseModel):
    name: str
    is_n_gram: bool
    tf_score: float
    idf_score: float
    tf_idf_score: float



class KeywordGenerationResponse(BaseModel):
    success: bool
    document_name: str
    keywords: List[Keyword]
