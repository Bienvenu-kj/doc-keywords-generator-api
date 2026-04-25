from pydantic import BaseModel

from .term import Term


class Keyword(BaseModel):
    term: Term


