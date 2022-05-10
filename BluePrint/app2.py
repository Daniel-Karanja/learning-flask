from flask import Blueprint

home=Blueprint("home",__name__)

@home.route("/")
def homes():
    return "<h1>This app 2 home</h1>"
