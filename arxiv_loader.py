import os
import arxiv
from langchain.document_loaders import PyPDFLoader
from pathlib import Path

FILE_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = FILE_PATH / "pdf_file"


def download_paper(a_id):
    paper = next(arxiv.Search(id_list=[a_id]).results())
    paper.download_pdf(dirpath=PDF_DIR, filename="{}.pdf".format(a_id))


def get_arxiv_paper(a_id):
    pdf_path = os.path.join(PDF_DIR, "{}.pdf".format(a_id))
    if os.path.isfile(pdf_path):
        pdf_loader = PyPDFLoader(pdf_path)
    else:
        download_paper(a_id)
        pdf_loader = PyPDFLoader(pdf_path)
    documents = pdf_loader.load_and_split()
    return documents
