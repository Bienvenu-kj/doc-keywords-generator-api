from ..ports.document_content_extractor import DocumentContentExtractor, DocumentSource


class DocumentContentExtractorService:
    def __init__(self, document_content_extractor:DocumentContentExtractor):
        self.document_content_extractor = document_content_extractor

    async def extract(self,source:DocumentSource)->str:
        return await self.document_content_extractor.extract(source)