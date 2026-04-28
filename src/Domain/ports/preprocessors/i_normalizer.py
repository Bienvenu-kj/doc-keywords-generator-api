from abc import ABC, abstractmethod


class Normalizer(ABC):
    @abstractmethod
    async def normalize(self, text:str) -> str:
        pass
