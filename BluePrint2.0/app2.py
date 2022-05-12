from flask import Blueprint

app2=Blueprint("app2",__name__)


@app2.route("/")
def index():
    return "<h1>This is the APP2 Index</h1>"


@app2.route("/new")
def new():
    return "<h1>This is the APP2 New</h1>"    