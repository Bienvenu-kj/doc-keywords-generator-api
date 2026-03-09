from pathlib import Path
import pdfplumber

def reader(document_path:Path):
    #print(f'Reading document: {document_path}')
    with open(document_path, 'rb') as f:
        pdf = pdfplumber.open(f)
        #first_page = pdf.pages[0]
        #print(first_page.chars[0])
        print(pdf.name)