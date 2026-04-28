import pytest

from src.Domain.services.preprocessors.term_constructor import TermConstructorService


@pytest.mark.asyncio
async def test_extract_terms_normalizes_text_and_removes_empty_tokens():
    service = TermConstructorService()

    terms = await service.construct_terms(list(term.lower() for term in ["Hello","HELLO","world","api"]))

    assert [term.name for term in terms] == ["api", "hello", "world"]


@pytest.mark.asyncio
async def test_extract_terms_returns_empty_list_for_empty_content():
    service = TermConstructorService()
    terms = await service.construct_terms([])

    assert terms == []
