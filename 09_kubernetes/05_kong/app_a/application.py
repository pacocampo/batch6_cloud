import requests
from os import environ
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/app-b')
def hello_appb():
    # Call to service DNS
    url = environ.get("APPB_SERVICE_HOST")
    port = environ.get("APPB_SERVICE_PORT")
    response = requests.get(f"http://{url}:{port}")
    return response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
