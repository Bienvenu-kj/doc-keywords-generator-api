from abc import ABC, abstractmethod


class Cleaner(ABC):
    @abstractmethod
    async def clean(self, content:str|list[str]) -> str:
        pass
