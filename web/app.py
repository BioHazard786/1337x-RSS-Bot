from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '!337x RSS Bot'


if __name__ == "__main__":
    app.run()