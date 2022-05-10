from flask import Flask
from app2 import *

app=Flask(__name__)

app.register_blueprint(home,url_prefix='')

@app.route("/")
def intro():
    return "<h1>This is the home page python app1.py</h1>"

if __name__=="__main__":    
    app.run(debug=True)