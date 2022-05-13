from enum import unique
from APP.app import db
from .Car import *


class User(db.Model):
    __tablename__ ="users"

    _id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text,nullable=False)
    email=db.Column(db.Text,nullable=False,unique=True)
    password=db.Column(db.Text,nullable=False)

    cars=db.relationship("Car",backref="user",lazy="dynamic")   

    def __init__(self,obj):
      
      self.name=obj["name"]
      self.email=obj["email"]
      self.password=obj["password"]
     
    # def __repr__(self):
    #     arr=[]
    #     for user in self:
    #         arr.append({'name':user.name, 'email':user.email, 'password':"#######"})
    #     print(arr)
    #     return arr
 
    def report_cars(self):
        print(f"Here are the cars of {self.name}")
        for car in self.cars:
            print(f"{car.model} {car.name}")


