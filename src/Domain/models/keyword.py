from pydantic import BaseModel

from Domain.models.document import Term


class Keyword(BaseModel):
    term: Term


