from ...ports.preprocessors.i_normalizer import Normalizer


class NormalizerService:
    def __init__(self, normalizer: Normalizer):
        self.normalizer = normalizer

    async def normalize(self, text: str) -> str:
        if len(text):
            return await self.normalizer.normalize(text)
        return ""
