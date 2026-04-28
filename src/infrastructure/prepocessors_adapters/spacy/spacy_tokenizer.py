from Domain.ports.preprocessors.i_tokenizer import Tokenizer

class TokenizerAdapter(Tokenizer):
    def tokenize(self, text:str, ng_gram:bool)->list:
        pass
