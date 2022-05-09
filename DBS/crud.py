from app import *


#CREATE READ UPDATE DELETE
##CRUD
####CREATE USER

# justin=User("Joseph Mwangi",23)
# samuel=User("Samuel Sam",34)

# ## These should BE None
# print(justin._id)
# print(samuel._id)

# ## Add The Users:

# # db.session.add(justin)

# db.session.add_all([justin,samuel])

# db.session.commit()

# #Session commit makes changes to the database

# print(justin._id)
# print(samuel._id)


#### READ ##

# q_all_users=User.query.all()
# q_first=User.query.get(1)

# print(q_first)
# print(q_all_users)

## Filter User

# q_filter_name=User.query.filter_by(name="Joseph Mwangi")
# q_filter=User.query.filter_by(age>23)

# print(q_filter.all())
# print(q_filter_name.all())


#### UPDATE  ##

# q_user=User.query.get(5)

# q_user.age=19
# q_user.name="Joseph Olintao"

# db.session.add(q_user)
# db.session.commit()

#### DELETE ##

# q_user=User.query.get(5)
# db.session.delete(q_user)
# db.session.commit()


##CREATE=POST
##READ==GET
##UPDATE===PUT
##DELETE===DELETE