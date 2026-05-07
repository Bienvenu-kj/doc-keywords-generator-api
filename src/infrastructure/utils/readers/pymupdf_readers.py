import pymupdf
from pymupdf import Document

from ....Domain.ports.custom_print import CustomPrintData
from ....Domain.ports.document_content_extractor import DocumentSource
from ..custom_printers.colorama_custom_printer import ColoramaCustomPrinter





class PymupdfReader:
    def __init__(self, source:DocumentSource):
       self.source = source

    async def read(self)-> Document|None:
        if self.source.is_a is "document":
            return await self.read_it_as_document(source=self.source)

        return await self.read_it_as_a_image()


    @staticmethod
    async def read_it_as_document(source:DocumentSource) -> Document|None:
        try:
            ColoramaCustomPrinter().print(CustomPrintData("warning",f"lecture du document : {source.name}"))
            doc= pymupdf.open(stream=source.content,filetype=source.document_type)
            ColoramaCustomPrinter().print(CustomPrintData("success",f"lecture du document : {source.name}, terminée !"))
            return doc
        except Exception as e:
            ColoramaCustomPrinter().print(CustomPrintData(status="error", message=str(e)))
            return None


    @staticmethod
    async def read_it_as_a_image() -> Document|None:
        return None




