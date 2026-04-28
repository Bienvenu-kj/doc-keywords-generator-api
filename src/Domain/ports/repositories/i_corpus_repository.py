from abc import ABC, abstractmethod
from pathlib import Path

from ...models.document import Document


class CorpusRepository(ABC):
    @abstractmethod
    async def load_documents(self, documents_path:str) -> list[Document]:
        pass

