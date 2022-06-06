from collections import namedtuple
from distutils import text_file
from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

words = []
defenitions = []

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', words=words, defenitions = defenitions )


@app.route('/add_word', methods=['POST'])
def add_word():
    text = request.form['text']
    
   
    data = json.load(open("data.json"))
    defenition = ""
    if text in data:
        defenition =  data[text][0]
    else:
       defenition = "There are no words like this"
    words.append(text)
    defenitions.append(defenition)
    return redirect(url_for('main'))