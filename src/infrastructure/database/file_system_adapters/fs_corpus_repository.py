from pathlib import Path

from ....Domain.models.document import Document
from ....Domain.ports.repositories.i_corpus_repository import CorpusRepository
from ...utils.readers import reader
from utils.document_content_preparators.pymupdf_prepare_document_content import pymupdf_get_document_content


class FileSystemCorpusRepository(CorpusRepository):
    async def load_documents(self, documents_path: Path) -> list[Document]:
        documents_path = Path(documents_path)
        if not documents_path.exists() or not documents_path.is_dir():
            # Le chemin n'existe pas ou n'est pas un dossier.
            return []

        all_documents: list[Document] = []

        for pdf_document_path in documents_path.rglob("*.pdf"):
            pdf_document = reader(pdf_document_path)
            if pdf_document is None:
                # Le PDF est illisible, on le saute pour continuer la construction.
                continue

            all_documents.append(
                Document(
                    name=pdf_document_path.name,
                    path=pdf_document_path.resolve().as_posix(),
                    doc_type=pdf_document_path.suffix.removeprefix("."),
                    content=pymupdf_get_document_content(pdf_document),
                    all_terms=[],
                    all_unique_terms=[]
                )
            )

        return all_documents
