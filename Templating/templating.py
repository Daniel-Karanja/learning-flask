from flask import Flask,render_template
from daily import *
import urllib3
import json

#Have a Back Button in the toDo.html to go back home

app=Flask(__name__)

toDo={
    "monday":"Play Football",
    "tuesday":"CODE",
    "wendesday":"Go To The Gym",
    "thursday":"Bake a cake",
    "friday":"Attend a dance class",
    "saturday":"Go To church",
    "sunday":"Movie Time"
}

@app.route('/')
def index():
    print(toDo)
    # http=urllib3.PoolManager()
    # r=http.request("GET","https://api.themoviedb.org/3/movie/popular?api_key=0d461ff3259abbbaff1984c64b8bb0c4&language=en-US")
    # print(json.loads(r.data.decode('utf-8')))
    return render_template("index.html",pageName="Index Page",toDo=toDo)

@app.route('/day/<day>')
def day(day):
    return render_template("toDo.html",pageName="To Do Page",key=day,todo=toDo[day])    


@app.route('/home')
def home():
    return render_template("home.html",title="Home Page")
   

@app.route('/sign/up')
def sign_up():
    return render_template("sign_up.html",title="Sign Page")
  
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',title="Not Found"),404

if __name__=="__main__":    
    app.run(debug=True)