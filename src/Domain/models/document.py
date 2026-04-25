from pathlib import Path
from typing import Literal, List

from pydantic import BaseModel

from .term import Term


class Document(BaseModel):
    name: str
    path: str|Path
    text: Literal["txt","pdf"]
    content: str
    terms: List[Term]


