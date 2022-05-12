from flask import Flask,session,request


app=Flask(__name__)
app.config['SECRET_KEY'] ='secret'

user={
    'name':"Dan",
    'phone':"2323423",
    'role':"Admin"
}
key='secret'

@app.route("/<token>",methods=["POST"])
def home(token):
    print(request.form)
    print(token)
    return {"home":"Sweet home"},201


if __name__=="__main__":    
    app.run(debug=True)