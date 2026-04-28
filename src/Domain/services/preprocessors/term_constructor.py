import re
from encodings import search_function

from ...models.term import Term


class TermConstructorService:
    async def construct_terms(self, document_terms: list[str]) -> list[Term]:
        all_unique_terms = self.get_all_unique_terms(document_terms)

        return [
            Term(
                name=term,
                is_n_gram=False,
                tf_idf_score=0,
                tf_score=0,
                idf_score=0,
            )
            for term in all_unique_terms
        ]

    @staticmethod
    def get_all_unique_terms(terms:list[str]) -> list[str] :
        return sorted(set(terms))
