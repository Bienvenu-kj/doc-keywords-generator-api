from pydantic import BaseModel


class Term(BaseModel):
    name: str
    isN_gram: bool
    TF_score: float
    IDF_score: float
    TF_IDF_Score: float
