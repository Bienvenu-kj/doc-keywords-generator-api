from fastapi import UploadFile

from ..dto.keyword_response import KeywordGenerationResponse
from ...Domain.models.keyword import Keyword
from ...Domain.models.term import Term


class GenerateKeywordsUseCase:
    @staticmethod
    async def execute(file: UploadFile) -> KeywordGenerationResponse:
        # En attendant le vrai pipeline TF-IDF, on conserve une réponse de demonstration.
        return KeywordGenerationResponse.from_domain(
            document_name=str(file.file.name),
            keywords=[
                Keyword(
                    term=Term(
                        name="intelligence artificielle",
                        is_n_gram=True,
                        tf_score=0.45,
                        idf_score=0.5,
                        tf_idf_score=0.95,
                    )
                ),
                Keyword(
                    term=Term(
                        name="Python",
                        is_n_gram=True,
                        tf_score=0.5,
                        idf_score=0.5,
                        tf_idf_score=0.87,
                    )
                ),
                Keyword(
                    term=Term(
                        name="APIe",
                        is_n_gram=True,
                        tf_score=0.5,
                        idf_score=0.5,
                        tf_idf_score=0.78,
                    )
                ),
            ],
        )
