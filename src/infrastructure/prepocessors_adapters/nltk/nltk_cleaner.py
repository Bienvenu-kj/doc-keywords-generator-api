from Domain.ports.preprocessors.i_cleaner import Cleaner


class CleanerAdapter(Cleaner):
    def clean(self, text_or_list_of_text:str|list[str]) -> str:
        pass