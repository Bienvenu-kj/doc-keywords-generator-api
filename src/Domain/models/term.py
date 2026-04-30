from pydantic import BaseModel


class Term(BaseModel):
        name:str
        is_n_gram:bool
        tf_score:float

        idf_score:float
        tf_idf_score:float

