
from typing import List, Any

from pydantic import BaseModel

from .term import Term


class Document(BaseModel):

    name:str
    path:str
    doc_type:str
    content:str
    all_terms:List[str]
    all_unique_terms:List[Term]

    def __setitem__(self, key:str, value:str|List[Term]|list[str])->"Document":
        setattr(self, key, value)
        return self






