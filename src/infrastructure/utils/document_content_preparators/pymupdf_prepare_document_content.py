from pymupdf import Document

from ..custom_print import print_c


async def pymupdf_get_document_content(document: Document | None) -> str:
    document_content = ""
    document_links = []

    # On récupère le contenu de chaque page et on garde les liens pour les retirer ensuite.
    if document is not None:
        print_c("success", f"Document : {document}")
        for page in document:
            document_links.extend(page.get_links())
            document_content += " "+ page.get_text()


    for link in document_links:
        if link.get("uri") is not None:
            document_content = document_content.replace(link["uri"], "")
    return document_content
