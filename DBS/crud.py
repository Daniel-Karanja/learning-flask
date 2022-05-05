from app import *

# ####CREATE USER

# justin=User("justin Mwangi",23)
# samuel=User("samuel",34)

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

## Filter User

# q_filter=User.query.filter_by(age>23)

# print(q_filter.all())


### UPDATE