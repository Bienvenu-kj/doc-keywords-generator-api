from abc import ABC, abstractmethod


class Tokenizer(ABC):
    @abstractmethod
    async def tokenize(self, text:str, n_gram:bool) -> list[str]:
        pass



