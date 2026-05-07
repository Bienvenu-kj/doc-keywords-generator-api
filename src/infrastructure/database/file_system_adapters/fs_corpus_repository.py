from pathlib import Path

from ....Domain.ports.document_content_extractor import DocumentSource
from ....Domain.models.document import Document
from ....Domain.ports.repositories.i_corpus_repository import CorpusRepository
from ....infrastructure.utils.document_content_preparators.pymupdf_prepare_document_content import InMemoryPymuPDFDocumentContentExtractor


class FileSystemCorpusRepository(CorpusRepository):
    async def load_documents(self, documents_path: str) -> list[Document]:
        _documents_path = Path(documents_path)
        if not _documents_path.exists() or not _documents_path.is_dir():
            # Le chemin n'existe pas ou n'est pas un dossier.
            return []

        all_documents: list[Document] = []

        for document_path in _documents_path.rglob("*.pdf"):
            document_bytes_content = document_path.read_bytes()
            document_source_data = DocumentSource(content=document_bytes_content, name=document_path.name,document_type=document_path.suffix.removeprefix("."))

            document_content = await InMemoryPymuPDFDocumentContentExtractor().extract(document_source_data)
            if document_content is None or document_content == '':
                # Le PDF est illisible, on le saute pour continuer la construction.
                continue

            all_documents.append(
                Document(
                    name=document_path.name,
                    path=document_path.resolve().as_posix(),
                    doc_type=document_path.suffix.removeprefix("."),
                    content=document_content,
                    all_terms=[],
                    all_unique_terms=[]
                )
            )

        return all_documents
