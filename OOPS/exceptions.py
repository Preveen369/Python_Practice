# errors and exceptions in PYTHON

# errors: it occurs when the rules (syntaxes) of program is broken.
# exception: is an event, which occurs during the execution of a program 
# that disrupts the normal flow of the program's instructions

# examples of errors: syntax errors (python always checks this first)
# examples of exceptions: logical errors (type, assertion, name, etc.,)
# exceptions could be handled using try, except blocks (built-in, custom) way

# print(10)
# print(10/0)   --> then logical error [EXCEPTION] occurs
# print(        --> first syntax error [ERROR] occurs

# built-in exception handling using try..except.. blocks:
# TO_NOTE: when try doesn't raise any exception, else block executes and 
# irrespective of any exceptions may/not occured, finally block executes
try:
    print("x + y")
    print(10/0)
except NameError:
    print("Variables Undefined!!")
except ZeroDivisionError:
    print("Zero div Not Allowed!!")
else:
    print("Division finished...")
finally:
    print("Finally is executed...")


# custom exception handling using user defined Exception Class   
class InvalidNumber(Exception):
    pass 

num = int(input("Enter the number (0-10): "))
if (0 <= num <= 10):
    print(f"Entered num is: {num}")
else:
    raise InvalidNumber(f"{num} doesn't lie in range (0-10)!!")
