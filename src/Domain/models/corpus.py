
from typing import List
from .document import Document


class Corpus:
    def __init__(self, documents: List[Document]):
        self.documents= documents

