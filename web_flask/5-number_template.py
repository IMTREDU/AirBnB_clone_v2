#!/usr/bin/python3
"""
Flask web application that displays various text for specified routes.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route for the root URL that returns "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route for the /hbnb URL that returns "HBNB".
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route for the /c/<text> URL that returns "C " followed by the value of the text variable.
    Underscores in <text> are replaced with spaces.
    """
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route for the /python/<text> URL that returns "Python " followed by the value of the text variable.
    Underscores in <text> are replaced with spaces. The default value of <text> is "is cool".
    """
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Route for the /number/<n> URL that returns "<n> is a number" only if n is an integer.
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route for the /number_template/<n> URL that returns an HTML page only if n is an integer.
    The HTML page displays "Number: n" inside an H1 tag.
    """
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
