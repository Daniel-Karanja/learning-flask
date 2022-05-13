from flask_bcrypt import Bcrypt

### CREATE #####

bcrypt=Bcrypt()


def create_user(obj,Model,db):
    if 'password' in obj:
      newPass=bcrypt.generate_password_hash(obj['password'])
      obj['password']=newPass
      print(obj)
      db.session.add(Model(obj))
      db.session.commit()
      return {'status':True,'payload':'Finished hashing password'}
    return {'status':False,'payload':'obj doesnt contain password'}  
    

def create_data(obj,Model,db):
      db.session.add(Model(obj))
      db.session.commit()



def get_all_users(Model):
    arr=[]
    users=Model.query.all()
    for user in users:
        print(user)
        arr.append({'name':user.name, 'email':user.email, 'password':"#######","id":user._id,'del':f'http://127.0.0.1:5012/dashboard/user/delete/{user._id}'})
    
    return arr

    