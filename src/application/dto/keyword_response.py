from typing import List

from pydantic import BaseModel

from ...Domain.models.keyword import Keyword


class KeywordTermResponse(BaseModel):
    name: str
    is_n_gram: bool
    tf_score: float
    idf_score: float
    tf_idf_score: float


class KeywordResponse(BaseModel):
    term: KeywordTermResponse


class KeywordGenerationResponse(BaseModel):
    success: bool
    document_name: str
    keywords: List[KeywordResponse]

    @classmethod
    def from_domain(
        cls,
        document_name: str,
        keywords: List[Keyword],
    ) -> "KeywordGenerationResponse":
        return cls(
            success=True,
            document_name=document_name,
            keywords=[
                KeywordResponse(
                    term=KeywordTermResponse(
                        name=keyword.term.name,
                        is_n_gram=keyword.term.isN_gram,
                        tf_score=keyword.term.TF_score,
                        idf_score=keyword.term.IDF_score,
                        tf_idf_score=keyword.term.TF_IDF_Score,
                    )
                )
                for keyword in keywords
            ],
        )
