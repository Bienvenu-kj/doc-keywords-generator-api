from ....Domain.ports.preprocessors.i_normalizer import Normalizer


class InMemoryNativeNormalizer(Normalizer):
    async def normalize(self, content:str) -> str:
        return content.lower()