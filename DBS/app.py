import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)


#Data Base Model

class User(db.Model):
    
    #Manual Table Name users
    __tablename__ ='allusers'

    #Create Columns For Users
    _id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)


    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __repr__(self):
        return f"id: {self._id} name: {self.name} age: {self.age}"


@app.route("/")
def intro():
    #home.html
    return "<h1>Welcome</h1>"


if __name__=="__main__":    
    app.run(debug=True)