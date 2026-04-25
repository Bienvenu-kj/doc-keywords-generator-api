from pydantic import BaseModel
from typing import List
from .document import Document


class Corpus(BaseModel):
    documents: List[Document]

