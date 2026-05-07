from pydantic import BaseModel
from ...Domain.models.term import Term


class PreprocessingResult(BaseModel):
    all_terms:list[str]
    all_unique_terms:list[Term]