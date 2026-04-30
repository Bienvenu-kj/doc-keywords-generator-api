from pathlib import Path
from typing import Literal

import pymupdf
from fastapi import UploadFile
from pymupdf import Document

from ..custom_print import print_c





class PymupdfReader:
    def __init__(self, document_path: Path|str|None=None , document_type: Literal['pdf','txt']='pdf', is_a:Literal['image','document']='document', uploaded_document: UploadFile = None):
        self.document_path = document_path
        self.is_a = is_a
        self.document_type = document_type
        self.uploaded_document = uploaded_document


    async def read(self)-> Document|None:
        if self.is_a == "document":
            if self.document_path is not None:
                return await self.read_doc_from_fs(document_path=self.document_path,doc_type=self.document_type)
            elif self.uploaded_document is not None:
                return await self.read_uploaded_file(uploaded_document=self.uploaded_document,doc_type=self.document_type)
        return None


    @staticmethod
    async def read_doc_from_fs(document_path: Path|str, doc_type:Literal["pdf","txt"]) -> Document|None:
        try:
            # with pymupdf.open(document_path,filetype=doc_type) as doc:
            doc= pymupdf.open(document_path,filetype=doc_type)
            return doc
        except Exception as e:
            print_c(status="error", message=str(e))
            return None


    @staticmethod
    async def read_uploaded_file(uploaded_document: UploadFile, doc_type:str) -> Document|None:
        try:
            doc_content = await uploaded_document.read()
            print_c("success",f"type du document {uploaded_document.content_type}")

            # with pymupdf.open(stream=doc_content,filetype=doc_type) as doc:
            doc = pymupdf.open(stream=doc_content,filetype=doc_type)
            return doc
        except Exception as e:
            print_c(status="error", message=str(e))
            return None




