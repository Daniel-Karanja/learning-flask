import os
print(__file__)
print(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))
k=os.path.join("home/some/some","mycoolfule","myapp.py")
print(basedir)
print(k)