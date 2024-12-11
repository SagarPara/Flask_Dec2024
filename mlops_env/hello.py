from flask import Flask

app = Flask(__name__)


#API endpoints
@app.route("/")
def hello_world():
    return "<h1>Hello there!!!</h1>"


@app.route("/ping", methods=["GET"])
def ping():
    return "Why are you pining me"

