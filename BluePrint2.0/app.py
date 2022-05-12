from flask import Flask
from app2 import app2

app=Flask(__name__)
app.register_blueprint(app2,url_prefix="/app2")


@app.route("/")
def index():
    #home.html
    return "<h1>This is the app Index</h1>"


if __name__=="__main__":    
    app.run(debug=True)