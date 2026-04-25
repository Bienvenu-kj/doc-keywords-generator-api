from ...ports.tokenizer import Tokenizer


class TokenizerService:
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer

    async def tokenize(self, text: str, n_gram: bool) -> list:
        if len(text):
            return self.tokenizer.tokenize(text, n_gram)
        return []
