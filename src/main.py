import os
import sys

from flask import Flask, render_template, request

sys.path.append('../')
from src.vbe_fci.fci import fci_util

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def index():
    fci_message = ''
    if request.method == 'POST':
        if request.form['submit'] == 'submit_fci_string':
            text = request.form['string_fci']
            fci_message = fci_util(text)

    return render_template('index.html', fci_message=fci_message)


'''
@app.route('/result', methods=['POST, GET'])
def result():
    if request.method == 'POST':
        fci_result = request.form
        return render_template("result.html", result=fci_result)
'''

if __name__ == '__main__':
    # print(os.path.dirname(os.path.realpath(__file__)))
    app.run(debug=True)
