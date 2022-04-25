from flask import Flask
from daily import *

#Assignment.
#Have a back Button form to "day" to go back to home.
#Handle case error.
#Handle Short form erroes. Eg tuesday short form tue

app=Flask(__name__)

@app.route("/")
def intro():
    #home.html
    return get_all_to_do()

@app.route("/day/<name>")
def day(name):
    return get_the_to_do(name)

if __name__=="__main__":    
    app.run(debug=True)