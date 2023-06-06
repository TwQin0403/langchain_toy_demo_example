from flask import Flask, render_template, request, jsonify, url_for
from main import main
import shutil
import os
from latex_generator import generate_latex_files
from pathlib import Path

app = Flask(__name__)
FILE_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = FILE_PATH / "output"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    arxiv_id = request.form.get('arxiv_id')
    filetype = request.form.get('filetype')

    if filetype == "pdf":
        main(arxiv_id)
        shutil.move(os.path.join(OUTPUT_DIR, 'temp.pdf'),
                    os.path.join("static", "{}.pdf".format(arxiv_id)))
        # file_path = os.path.join("static", "{}.pdf".format(arxiv_id))
    elif filetype == "tex":
        # your function to generate tex file
        generate_latex_files(arxiv_id)
        shutil.move(os.path.join(OUTPUT_DIR, 'temp.tex'),
                    os.path.join("static", "{}.tex".format(arxiv_id)))
        # file_path = os.path.join("static", "{}.tex".format(arxiv_id))

    # return the file URL instead of the file content
    return jsonify({
        'file_url':
        url_for('static', filename="{}.{}".format(arxiv_id, filetype))
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4321)
