from flask import Flask,render_template,request,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
# Make a navigation using a base template. 
# The color of the active button changes.

app=Flask(__name__)


app.config["SECRET_KEY"] ="mykey"

class InfoForm(FlaskForm):
    email=StringField("Enter Your Email Address")
    password=StringField("Enter Your Password")
    submit=SubmitField()

@app.route("/")
def home():
    return render_template('index.html',myTitle="Index Page")

@app.route("/signup")
def signup():
    return render_template('signup.html',myTitle="Sign Up Page")

@app.route("/confirm")
def confirm():
    print(request)
    email=request.args.get('email')
    password=request.args.get('password')
    check=request.args.get('check')
    return render_template('confirm.html',myTitle="Confirm",email=email,password=password,check=check)

@app.route('/better/sign_up',methods=['GET','POST'])
def better_sign_up():
    form=InfoForm()
    #    print(form.is_submitted())
    #    print(form.validate())
    if form.is_submitted():
        # print("The Form is Submitted")
        session["email"]=form.email.data
        session["password"]=form.password.data
        return redirect(url_for("thanks"))

    return render_template("better_sign_up.html",form=form)


@app.route('/thanks')
def thanks():
    return render_template("thanks.html")


if __name__=="__main__":    
    app.run(debug=True)