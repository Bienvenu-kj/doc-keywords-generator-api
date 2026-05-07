from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal


@dataclass
class DocumentSource:
    name: str
    content: bytes
    document_type: str
    is_a:Literal['image', 'document'] = 'document'


class DocumentContentExtractor(ABC):
    @abstractmethod
    async def extract(self, source:DocumentSource)->str:
        pass
