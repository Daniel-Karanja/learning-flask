from flask import Flask,session
import jwt
from datetime import datetime

app=Flask(__name__)
app.config['SECRET_KEY'] ='secret'

user={
    'name':"Dan",
    'phone':"2323423",
    'role':"Admin"
}
key='secret'

@app.route("/")
def home():
    
    if 'jwt' in session:
       token=session['jwt']
       try:
           user=jwt.decode(token,key,algorithms="HS256")
           print(user)
           return f"<h1> Hey Your Token is Valid</h1><p>{token}</p>"
       except Exception as e:
             return f"<h1> Hey Token Expired</h1><p>{e}</p>"
       
    return f"<h1>Please Login</h1>"

@app.route("/login")
def login():
    exp=int(datetime.now().timestamp())+10
    jwt_token=jwt.encode({'user':user,'exp':exp},key,algorithm="HS256")
    session['jwt']=jwt_token
    return f"<h1>This is the login page</h1><p>{jwt_token}</p>"


if __name__=="__main__":    
    app.run(debug=True)