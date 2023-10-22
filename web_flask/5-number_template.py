#!/usr/bin/python3
"""Starting Flask """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_():
    """: display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ display text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n=None):
    """Allow request if path variable is a valid integer
    """
    return str(n) + ' is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_if_number(n):
    """handling numbers only"""
    path = '5-number.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
