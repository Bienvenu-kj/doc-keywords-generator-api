from ....Domain.ports.preprocessors.i_tokenizer import Tokenizer


class InMemoryNativeTokenizer(Tokenizer):
    async def tokenize(self,content:str, ng_gram:bool) -> list[str]:
        return [
            term.strip()
            for term in content.split(" ")
            if term.strip()
        ]