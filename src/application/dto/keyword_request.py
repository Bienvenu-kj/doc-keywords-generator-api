from pathlib import Path
from typing import Literal

from pydantic import BaseModel, PositiveInt


class KeywordGenerationRequest(BaseModel):
    document_name: str
    document_type: Literal["txt", "pdf"]
    document_path: str | Path
    keyword_count: PositiveInt
