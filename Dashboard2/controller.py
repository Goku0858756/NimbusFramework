__author__ = 'N05F3R4TU'
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)


@app.route('/login')
def login():
    return "Login Pagina"

@app.route('/')
@app.route('/home')
def homepage():
    # return "This is the Hopepage"
    return render_template('index.html')

def main(host=None, port=None, debug=True):
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()