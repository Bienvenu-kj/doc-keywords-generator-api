
from typing import List

from pydantic import BaseModel

from .document import Document


class Corpus(BaseModel):
    documents: List[Document]


