from Domain.ports.preprocessors.i_normalizer import Normalizer


class NormalizerAdapter(Normalizer):
    def normalize(self, text:str)->str:
        pass