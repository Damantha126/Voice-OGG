import os
import glob
from os.path import basename, dirname, isfile

from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory

UPLOAD_FOLDER = "./Voice"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/<filename>')
def uploaded_file(filename):
  try:
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
  except:
    return("File Not dound")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True, debug=True) 
