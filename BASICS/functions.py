# functions in python:

# functions -> the reusable part of code to perform specific task
# the block of statments under function gets executed only when called

def greetUser():
    print("Welcome to world of Roblox...")
    print("Hope you enjoy it so!!")

greetUser()
# greetUser()

# print("namaste")

# methods -> set of functions which runs on objects of particular class
# functions are independent while methods are dependent of objects


# "functions act as first class objects in python"
# returning values from the functions:

# why used ?? -> to return(transfer) the value from 
# function back to the function called

def count():
    num, num1 = 10, 20
    # print(num)
    return (num, num1)

# # assigning function to variable
# val, val1 = count()   
# print(val, val1)

print(count())
print(type(count()))

# print(count())
# count()


# passing function as argument to other functions:
def multiply(a, b):
    res = a * b
    return res

def divide(a, b):
    res = a / b
    return res

def calculate(func, x, y):
    return func(x, y)

num1 = 10
num2 = 5
product = calculate(multiply, num1, num2)
quotient = calculate(divide, num1, num2)

print(product, quotient)


# formal arguments (parameters) & actual arguments(arguments)
def addition(a, b): # parameters (variables defined)
    return a + b

res1 = addition(4, 5)   # arguments (values sent to func)
print(res1)

# positional (required) arguments
def subtraction(a,b):
    return a - b

res2 = subtraction(9,5) # requires equal position of args
# res2 = subtraction()  -> results TypeError (missing args)
print(res2)


# PASS BY VALUE AND PASS BY OBJECT(REFERENCE)

# pass by values -> when immutable type (passed)
def my_function1(text):
    output = 'Hello'
    output += text
    return output

text = "World"
print(text)
my_function1(text)   # copy of value is created while passed
print(text)     # original object's val, remains unchanged


# pass by reference(object) -> when mutable type (passed)
def my_function2(checklist, item):
    return checklist.append(item)

my_todolist = ['System', 'Bills', 'Bagpack']
itemToAdd = "Office Items"
print(my_todolist)
my_function2(my_todolist, itemToAdd)   # reference of obj is passed
print(my_todolist)     # modified changes gets reflected


# Arbitrary Arguments (* args)  VARIABLE LENGTH ARGS
def my_function3(*name):    # parameter not defined
    for each_name in name:
        print("Hello", each_name)

my_function3("Sofen", "Vishaal")
my_function3("Sofen", "Vishaal", "Preveen")

# Default Arguments (eg,. a=4, b=5)
def func_play(a=6, b=5):
    return a, b

n1,n2 = func_play(4)
print(n1, n2)


# Keyword Arguments when Parameters Known 
def my_function4(name, age):
    print(name,age)

my_function4(age=22, name="Pranesh")


# Arbitrary Keyword Arguments (**kwargs) VARIABLE KWARGS
def my_function5(**details):
    for field, value in details.items():
        print(field, ":", value)

my_function5(name="Kiran", age=20, city="Sivaganga")


# Scopes of Variable:
# 1) Global Scope -> (used inside & outside func)
# 1) Local Scope -> (used only inside func)

x=10    # x is global scoped
print(x)

def func(): # x is local scoped
    global x # x's scope is changed to global
    x=5
    return x

print(func())
print(x)


# recursive function: a function when calls itself
# max. recursion depth limit -> 1000
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

num = 5
print(factorial(num))