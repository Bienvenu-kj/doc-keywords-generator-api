
from typing import List, Any
from .term import Term


class Document:

    def __init__(self, name:str, path:str, doc_type:str, content:str, all_unique_terms:List[Term]):
        self.name = name
        self.path = path
        self.type = doc_type
        self.content = content
        self.all_unique_terms = all_unique_terms

    def __setitem__(self, key:str, value:str|List[Term])->"Document":
        setattr(self, key, value)
        return self






