import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)

user="postgres"
password="root"
host="44.200.116.238"
database="syntax"

##postgresql://garnjjmfrdudcx:042ad00f0836af0afd40ee473685d9e0b4c7c90c2b027ec747426b87ae73b0bd@ec2-52-3-200-138.compute-1.amazonaws.com:5432/dbvjvtrtuotqja

uri=f"postgresql://{user}:{password}@{host}/{database}"

app.config["SQLALCHEMY_DATABASE_URI"] =uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


db=SQLAlchemy(app)
Migrate(app,db)

class Employee(db.Model):

    __tablename__ ="employees"

    _id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text,nullable=False)
    phone=db.Column(db.BIGINT,nullable=False,unique=True)
    age=db.Column(db.Integer)
    
    ###One Employee Can HAve Multiple Cars
    ## This relation is one to many.
    cars=db.relationship("Car",backref="user",lazy="dynamic")   

   ## One Employee can only have one Spause
    spouse=db.relationship("Spause",backref="user",uselist=False)
    

    def __init__(self,obj):
      
      self.name=obj["name"]
      self.phone=obj["phone"]
      self.age=obj["age"]
     
    def __repr__(self):
        if self.spouse:
            return f"_id: {self._id} name:{self.name} spause==true spause: %{self.spouse.name}  %"
        
        return f"_id: {self._id} name:{self.name} not married:"
 
    def report_cars(self):
        print(f"Here are the cars of {self.name}")
        for car in self.cars:
            print(f"{car.model} {car.name}")



class Car(db.Model):

    __tablename__ ="cars"

    _id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text,nullable=False)
    model=db.Column(db.Text,nullable=False,default="Toyota")
    cc=db.Column(db.Integer,nullable=False)
    
    ### Employee Foreign Key ###
    owner=db.Column(db.Integer,db.ForeignKey("employees._id"))

    def __init__(self,obj):
      
       self.name=obj["name"]
       self.model=obj["model"]
       self.cc=obj["cc"]
       self.owner=obj["_id"]

   

class Spause(db.Model):

    __tablename__ ="spauces"

    _id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text,nullable=False)
    phone=db.Column(db.Integer,nullable=False,unique=True)
    age=db.Column(db.Integer)
    
    #One Employee Can Only One Spause
    ## This relation is one to many.
    spause=db.Column(db.Integer,db.ForeignKey("employees._id"))

    def __init__(self,obj):
      
       self.name=obj["name"]
       self.phone=obj["phone"]
       self.age=obj["age"]
       self.spause=obj["_id"]

if __name__=="__main__":    
    app.run(debug=True)