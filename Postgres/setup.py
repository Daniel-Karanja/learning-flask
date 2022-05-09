from APP.app import db

#CREATE ALL TABLES

def create_all_tables():
    db.create_all()