from app import *

#############
### CRUD ####
#############

##############
####CREATE####
##############


user=User("Maggy Migg",18,2546786323)

db.session.add(user)
db.session.commit()


print(User.query.all())
