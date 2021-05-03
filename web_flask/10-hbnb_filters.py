#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Display a HTML"""
    states = storage.all(State).values()
    amens = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amens=amens)


@app.teardown_appcontext
def remove_Alchemy(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
