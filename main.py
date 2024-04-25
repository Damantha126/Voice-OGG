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
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
  except:
    return("File Not dound")

def __list_all_voices():
    mod_paths = glob.glob("./Voice/*.ogg")

    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".ogg")
    ]

    return all_voices
  

@app.route('/ogg')
def uploaded_file(filename):
  try:
    all_voices = sorted(__list_all_voices())
    return(all_voices)
  except:
    return("Error")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True, debug=True) 
