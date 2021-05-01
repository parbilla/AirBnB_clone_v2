#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Display Hello"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Display C followed by text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def py_text(text='is cool'):
    """Display Python followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Display a number"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run()
