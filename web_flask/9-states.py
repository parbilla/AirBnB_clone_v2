#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_cities(id=None):
    """Display a HTML with the list of cities of a state"""
    st_city = storage.all(State)
    key = "{}.{}".format('State', id)
    return render_template('9-states.html', st_city=st_city, id=id, key=key)


@app.teardown_appcontext
def remove_Alchemy(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
