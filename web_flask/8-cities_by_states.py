#!/usr/bin/python3
""" A Flask web application that displays cities by states. """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays a HTML page with a list of all State objects. """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
