from app import *


obj={"name":"Yusuf Hajiu","phone":4564676545,"age":45}

db.session.add(Employee(obj))

db.session.commit()