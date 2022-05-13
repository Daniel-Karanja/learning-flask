
def create_dbs():
    from APP.app import db
    from .Car import Car
    from .User import User

    print("Creating The Data Base")
    db.create_all()
