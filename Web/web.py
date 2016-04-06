from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    getal = 24

    return "Haoooo"

def start_web(host='localhost', port=8000, debug=True):
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    start_web()
