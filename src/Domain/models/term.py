from pydantic import BaseModel


class Term(BaseModel):
    name: str
    isN_gram: bool
    TFscore: float
    IDFscore: float
    TF_IDF_Score: float
