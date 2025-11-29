# lambda functions in python:
# small and anonymous function, without name
# it can hold any number of arguments, one expression
# syntax=> lambda arguments : expression

# f1 = lambda x, y, z : x + y + z
# print(f1(3,4,5))

# def f1(x):
#     return x + 10
# print(f1(5))

# example: find the powers of number;
def power(n):
    return lambda a : a ** n

square = power(2)
cube = power(3)
fourth_pow = power(4)

print(square(2))
print(cube(2))
print(fourth_pow(2))



# decorators in python;

# funct decorator: a funct(fun1) is wrapped inside another funct(wrapper)
# when original funct(fun1) is passed as an argument to decorator funct
# to enhance(modify) the behaviour of original funct (fun1), easily...

def my_decorator(func):
    def wrapper():
        func()
        print("My aim is to become an AUDITOR")
    return wrapper

 # wrapping myfun1() in decorator and enhances myfun1()'s behaviour
@my_decorator  
def myfun1():
    name = "PREVEEN"
    print("My name is " + name)

def myfun2():
    name = "PRANESH"
    print("My friend name is " + name)
    

# execution of ""decorator functions"":
myfun1()    # function with enhanced behviour
myfun2()    # normal function

# when '@' decorator symbol is not used: 
# decorated = my_decorator(myfun1)  # send func to decorator
# decorated()    # calls the decorated function
# funct()     # calls & results decorated function


# generators in python: functions that pauses execution (middle)
# and holds the each current value (if required)
# and also remembers the execution point of values executed
# returns "iterator", to iterate over sequence of values each
# pause = """yield a value"""

def gener():
    yield 1
    yield 2
    yield 3

print(gener())

for x in gener():
    print(x)
    print(x, 'is a number')
    print(x, 'runs from a generator')
    print(x, 'will now move to next YIELD num')
    print("===================================")

x = gener()

print(next(x))
print(next(x))
print(next(x), '\n')

# eg: fibonacci series within specified limit:
def fibo(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a+b

# traverse the fibonacci values
x = fibo(5)
# print(next(x))
# print(next(x))

for x in fibo(100):
    print(x)

# Decorator: It is a design pattern that allows you to modify functionality of a 
# function by wrapping it in another function. The outer function is called decorator, 
# which takes the original function as an argument and returns a modified version of it.

# Generators :In Python, a generator is a function that returns an iterator that 
# produces a sequence of values when iterated over. Generators are useful when we 
# want to produce a large sequence of values, but we don't want to store all of 
# them in memory at once.