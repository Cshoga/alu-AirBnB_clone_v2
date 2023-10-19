#!/usr/bin/python3
""" A script that displays C """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello HBNB"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def change_text(text):
    changed_text = text.replace('_',' ')
    return f"C {changed_text}"


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
