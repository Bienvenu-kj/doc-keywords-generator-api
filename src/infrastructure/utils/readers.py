from pathlib import Path
import pymupdf
from pymupdf import Document

from .custom_print import print_c


def reader(document_path:Path|str) -> Document|None:
    """
    Une fonction d'aide, qui ouvre le document et le retourne

    :param document_path: qui est du doc_type `Path` ou `str`
    :return:
    """
    try:
        pdf = pymupdf.open(document_path)
        return pdf
    except Exception as e:
        print_c(status="error", message=str(e))
        return None