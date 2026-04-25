from pydantic import BaseModel
from typing import List
from Domain.models.document import Document, Term


class Corpus(BaseModel):
    documents: List[Document]

