from APP.app import db


class Car(db.Model):

    __tablename__ ="emp_cars"

    _id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text,nullable=False)
    model=db.Column(db.Text,nullable=False,default="Toyota")
    cc=db.Column(db.Integer,nullable=False)
    
    ### Employee Foreign Key ###
    owner=db.Column(db.Integer,db.ForeignKey("users._id"))

    def __init__(self,obj):
      
       self.name=obj["name"]
       self.model=obj["model"]
       self.cc=obj["cc"]
       self.owner=obj["_id"]

    def __repr__(self):
       return {'name':self.name, 'model':self.model, 'cc':self.cc,'owner':self.owner}
