from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
from app import views


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
