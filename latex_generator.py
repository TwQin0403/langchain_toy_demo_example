import subprocess
import os
from pathlib import Path

FILE_PATH = Path(os.path.dirname(os.path.abspath(__file__)))


def generate_latex_files(latex_string: str) -> None:
    # 將 LaTeX 字串寫入一個 .tex 檔案
    output_dir = FILE_PATH / "pdf_file"
    latex_file = os.path.join(output_dir, "temp.tex")

    with open(latex_file, "w") as f:
        f.write(latex_string)

    # 呼叫 pdflatex 來編譯 .tex 檔案
    subprocess.call([
        'pdflatex', '-interaction=nonstopmode',
        '-output-directory=' + str(output_dir),
        str(latex_file)
    ])
