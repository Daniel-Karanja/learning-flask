import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))

app.config["SQLACHEMY_DATABASE_URI"]="sqlite:///sql"+os.path.join(basedir,'data.sqlite')
app.config["SQLACHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

@app.route("/")
def intro():
    #home.html
    return "<h1>Welcome</h1>"


if __name__=="__main__":    
    app.run(debug=True)