#!/usr/bin/python3
""" A Flask web application that displays states and their cities. """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Displays a HTML page with a list of states or a specific state and cities. """
    states = storage.all(State).values()
    if id is None:
        states = sorted(states, key=lambda state: state.name)
        return render_template('9-states.html', states=states, state=None)
    else:
        state = None
        for s in states:
            if s.id == id:
                state = s
                break
        if state:
            return render_template('9-states.html', state=state, states=None)
        else:
            return render_template('9-states.html', state=None, states=None)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
