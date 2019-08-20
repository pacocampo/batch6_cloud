import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/app-b')
def hello_appb():
    response = requests.get("http://appb:5000/")
    return response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
