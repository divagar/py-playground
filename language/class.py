import string
import collections
from typing import Any

class User:
    def __init__(self):
        self.firstname = "Divagar"
        self.lastname = "Mohandass"
        self.age = 37

    def __str__(self):
        return "Firstname: {0}, Lastname: {1}, Age: {2}, firstnamelastname: {3}".format(self.firstname, self.lastname, self.age, self.firstnamelastname)
    
    def __getattr__(self, attr):
        if(attr == "firstnamelastname"):
            return self.firstname + " " + self.lastname
        else:
            pass
    
    def __setattr__(self, attr, val):
        if(attr == "newfirstname"):
            self.firstname = val
        elif(attr == "newlastname"):
            self.lastname = val
        elif(attr == "newage"):
            self.age = val
        else:
            super().__setattr__(attr, val)
        

myUser = User()
print(myUser)
myUser.newfirstname = "Tan"
myUser.newlastname = "Div"
myUser.newage = 6
print(myUser)