#!/usr/bin/python3
""" A script that displays Hello HBNB on the page """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello HBNB"

if __name__ == "__main__":
    app.run(strict_slashes=False)
