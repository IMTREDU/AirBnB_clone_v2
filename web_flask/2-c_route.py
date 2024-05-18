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
    """ Route for the /c/<text> URL that returns "C " followed by the value of the text variable.
    Underscores in <text> are replaced with spaces. """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
