from flask import Flask,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .car.cars import car
from .user.user import user




app=Flask(__name__)
app.config['SECRET_KEY']='secret_key'
app.register_blueprint(car,url_prefix='/dashboard/car')
app.register_blueprint(user,url_prefix='/dashboard/user')


user="postgres"
password="root"
host="44.200.116.238"
database="syntax"

uri=f"postgresql://{user}:{password}@{host}/{database}"

app.config["SQLALCHEMY_DATABASE_URI"] =uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


db=SQLAlchemy(app)
Migrate(app,db)

@app.route("/")
def intro():
    return redirect(url_for('user.index'))


def create():
    app.run(debug=True,port="5012")