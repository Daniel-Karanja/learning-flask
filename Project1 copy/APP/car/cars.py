from flask import Blueprint,render_template

car=Blueprint("car",__name__,static_folder="./../static",template_folder="./../templates")


@car.route("/")
def index():
    return render_template("cars/index.html",active=["","","w3-blue",""],page_title="All Cars")

@car.route("/add")
def add():
    return render_template("cars/add.html",active=["","","","w3-blue"],page_title="Add Car")    