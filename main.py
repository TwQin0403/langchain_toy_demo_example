from pdf_handler import summary_latex
from latex_generator import generate_latex_files


def main(arxiv_id: str):
    latex_string = summary_latex(arxiv_id)
    generate_latex_files(latex_string)
