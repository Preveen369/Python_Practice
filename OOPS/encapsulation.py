# encapsulation in PYTHON:
# It is used to protect(hide) the variables, methods of class
# from the outside, for secured access

class UserDetails:
    __name = "Preveen S"
    __phone_num = 9488960369
    __deg_dept = "BTech & IT"
    __email = "spreveen123@gmail.com"

    def displayDetails(self):
        print(f"user name: {self.__name}")
        print(f"user phone_num: {self.__phone_num}")
        print(f"user deg_dept: {self.__deg_dept}")
        print(f"user email: {self.__email}")

user = UserDetails()
# able to access user's details only through method:
user.displayDetails()
    