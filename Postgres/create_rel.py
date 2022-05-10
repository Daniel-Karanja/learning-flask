from app import *


# obj={"name":"Manndy yusuf","phone":7675654545,"age":23}

# db.session.add(Employee(obj))

# db.session.commit()

# print(Employee.query.all()[0].name)


yusuf=Employee.query.filter_by(phone=4564676545).first()




print(yusuf._id)

yusuf.report_cars()

# obj={"name":"cx5","model":"Mazda","cc":2000,"_id":yusuf._id}

# db.session.add(Car(obj))
# db.session.commit()