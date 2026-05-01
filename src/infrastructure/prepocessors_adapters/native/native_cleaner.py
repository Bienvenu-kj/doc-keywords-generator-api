import re
from ....Domain.ports.preprocessors.i_cleaner import Cleaner


class InMemoryNativeCleaner(Cleaner):
    async def clean(self, content:str) -> str:
        return re.sub(
             pattern=r"[0-9+></.=%{}*^$)(&~@?`\§!|£¨;:,'\"«»…]",
             repl="",
             string=(
                 content
                 .replace("\n", " ")
                 .replace("\t", " ")
                 .replace("\r", " ")

             ))