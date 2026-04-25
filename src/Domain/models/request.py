from pathlib import Path
from typing import Literal

from pydantic import BaseModel, PositiveInt


class RequestForKeywordGen(BaseModel):
    documentName: str
    documentType : Literal["txt","pdf"]
    documentPath: str | Path
    howManyKeyword: PositiveInt


