from ....Domain.ports.custom_print import CustomPrintData
from ....Domain.ports.document_content_extractor import DocumentSource
from ....Domain.ports.document_content_extractor import DocumentContentExtractor
from ..custom_printers.colorama_custom_printer import ColoramaCustomPrinter

from ..readers.pymupdf_readers import PymupdfReader



class InMemoryPymuPDFDocumentContentExtractor(DocumentContentExtractor) :
    async def extract(self,source:DocumentSource)->str:
        document_links = []
        document_content = ''

        # On récupère le contenu de chaque page et on garde les liens pour les retirer ensuite.
        document = await PymupdfReader(source=source).read()


        # on affiche quelques logs
        if document is not None :
            ColoramaCustomPrinter().print(CustomPrintData("success",f"La préparation du contenu du document : {source.name}"))


        if document is not None:
            for page in document:
                document_links.extend(page.get_links())
                document_content += " "+ page.get_text()
        else :
            return ''

        # on retire tous les liens s'il y en a
        for link in document_links:
            if link.get("uri") is not None:
                document_content = document_content.replace(link["uri"], "")

        return document_content
