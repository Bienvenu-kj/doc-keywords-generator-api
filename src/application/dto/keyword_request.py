from typing import Annotated

from fastapi import UploadFile, File
from pydantic import BaseModel, PositiveInt, Field


class KeywordGenerationRequest(BaseModel):
    max_keywords_count: PositiveInt = Field()
    file: Annotated[UploadFile,File()]

