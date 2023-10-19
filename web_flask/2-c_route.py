#!/usr/bin/python3
""" Script that displays C followed by the value of the text variable """
from flask import Flask
app = Flask(__main__)

@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def change_name(text):
    changed_text = text.replace('_', ' ')
    

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
