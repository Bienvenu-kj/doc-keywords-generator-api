from ...ports.preprocessors.i_cleaner import Cleaner


class CleanerService:
    def __init__(self, cleaner: Cleaner):
        self.cleaner = cleaner

    async def clean(self, text: str) -> str:
        if len(text):
            return await self.cleaner.clean(text)
        return ""