PRINTER_NAME = 'EPSON LX-310 ESC/P'

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import os
import win32print

app = Flask(__name__)
CORS(app)

@app.route('/dotmatrix/print', methods=['POST'])
def dotmatrix_print():
    printer_data = request.form['printer_data']
    p = win32print.OpenPrinter(PRINTER_NAME)
    job = win32print.StartDocPrinter(p,1, ("DOTMARIX",None, "RAW"))
    win32print.StartPagePrinter(p)
    win32print.WritePrinter(p, printer_data.encode())
    win32print.EndPagePrinter(p)
    return jsonify({'status': 'OK'})