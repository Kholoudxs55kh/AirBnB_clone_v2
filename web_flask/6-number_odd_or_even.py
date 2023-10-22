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
    """handling number only"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Render template based on conditional
    """
    flag = 'odd'
    if n % 2 == 0:
        flag = 'even'
    return render_template('6-number_odd_or_even.html', n=n, state=flag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
