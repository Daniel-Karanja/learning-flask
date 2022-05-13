from flask import Blueprint,render_template,redirect,url_for
from .form import New_User

baseUrl="http://127.0.0.1:5012"
dashboardUrl=f"{baseUrl}/dashboard"


user=Blueprint("user",__name__,static_folder="./../static",template_folder="./../templates")

dummy=[{'name':"some name", 'email':"some email"},{'name':"some name", 'email':"some email"},{'name':"some name", 'email':"some email"}]

@user.route("/")
def index():
    from APP.Model.User import User
    from APP.Model.crud import get_all_users

    data=get_all_users(User)

    
    
    # for user in s:
    #     print(user)
    return render_template("users/index.html",active=["w3-blue","","",""],page_title="All Users",headers=['Name','Email','Actions'],data=data)
  

@user.route("/add",methods=['GET','POST'])
def add():
    try:
        form=New_User()
        
        if form.is_submitted():
           
            from APP.app import db
            from APP.Model.User import User
            from APP.Model.crud import create_user
    
            obj={'name':form.name.data,'email':form.email.data,'password':form.password.data}
            print(obj)
            create_user(obj,User,db)
            return redirect(url_for('user.index'))
        return render_template("users/add.html",active=["","w3-blue","",""],page_title="Add User",form=form)    
    except Exception as e:
        print(e)
        return render_template("error.html",mess=e,active=["","","",""])

@user.route("/delete/<id>",methods=["GET", "POST"])
def delete(id):
    from APP.Model.User import User
    user=User.query.get(id)
    page_title=f"Delete User: {user.name}"
    return render_template("users/delete.html",active=["w3-blue","","",""],page_title=page_title,user=user.name)
