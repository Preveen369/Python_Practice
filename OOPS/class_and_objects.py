# OOPS (object oriented programming) Concepts Principles:
# Encapsulation: ability to hide the object's implementation details
# from the other codes of the program

# Inheritance: ability to give the properties and methods of 
# one class to the another class

# Polymorphism: ability of different objects to access the 
# same method in different kinds of ways

# Abstraction: ability to define and work with the objects based on 
# general characteristics rather than exact specific implementation

# using OOPS maintains the code very: readable, scalable, flexible, modular in nature
# every object(value) in python belongs to a certain class(data type)
# each object has an identity(address), attribute(property/value) & method(behaviour/fn) 

# creating a class
class Customer:
    # class attributes(variables): variables which are 
    # shared amongst all the objects of the class
    bank_name = "ABCD Bank"

    # instance variables: variables with unique values associated objects of class
    # local variables: variables which are specifically defined & accessed in methods

    # __init__(): creating a constructor method 
    def __init__(self, name, age, initial_amount): # local variable
        self.name = name                    # instance variable
        self.age = age                      # instance variable
        self.balance = initial_amount
        # print("Bank Account successfully created!!")
    
    def deposit(self, amount):  # local variable
        self.balance += amount
        print(f"Deposit of amount Rs.{amount} is done. Your updated balance: Rs.{self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal of amount Rs.{amount} is done. Updated balance: Rs.{self.balance}")

    # methods (functions) defined inside the class
    def greet(self): # takes current instance as parameter
        print(f"Hi {self.name}, welcome to ABCD Bank!!")
    
    # self: an extra parameter (python takes current instance (object's address) of class)
    # __init__(): a constructor method (used to initialize the instances of class)
    # This is first called whenever the object is created by calling the class method.


# # create an object
# c1 = Customer()
# print(c1.bank_name)
# c1.greet()            # normal way of accessing the instance method
# Customer.greet(c1)    # -> python intrepets like this by default

# c2 = Customer()
# # print(c2.bank_name)
# c2.greet()

# print(c1)
# print(type(c1))
# print(type(c2))


# understanding types of attributes, constructors:
c1 = Customer("Preveen", 21, 10000)
c1.greet()
c1.deposit(3000)
c1.withdraw(3000)

print()

c2 = Customer("Pranesh", 40, 30000)
c2.greet()
c2.deposit(100000)
c2.withdraw(50000)

# print(dir(c1))