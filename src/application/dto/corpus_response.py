from pydantic import BaseModel

from ...Domain.models.document import Document


class CorpusResponse(BaseModel):
    documents: list[Document]
