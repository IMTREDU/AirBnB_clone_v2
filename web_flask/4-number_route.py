#!/usr/bin/python3
""" Flask web application that displays various text for specified routes. """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Route for the root URL that returns "Hello HBNB!". """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Route for the /hbnb URL that returns "HBNB". """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Route for the /c/<text> URL that returns "C " then
    Underscores in <text> are replaced with spaces. """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Route for the /python/<text> URL that returns "Python " then
    Underscores in <text> are replaced with spaces. """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ Route for the /number/<n> URL that returns "<n> is a number" """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
