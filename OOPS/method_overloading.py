# method overloading in PYTHON:

# the overloading is concept of getting different results in method's behaviour when 
# different object's are passed in method's which share the same method name
# overloading is not diretly done in PYTHON:
    
def funct(val1, val2=None, val3=None):
    if val2 and val3:   # 3 args
        print(val1 * val2 * val3)
    elif val2:          # 2 args
        print(val1 + val2)
    else:               # 1 args
        print(val1)

funct(3, 6, 9)
funct(3, 6)
funct(3)


# DUCK TYPING philosophy in PYTHON: if an object behaves like DUCK, 
# quacks like DUCK, walks like DUCK then it is the DUCK by being
# irrespective of what object type it belongs, as long it is executable

# addition operation DUCK TYPING in python:
def add_operation(num1, num2):
    # performs addition / concatenation depending on object
    return num1 + num2  

print(add_operation(23, 34))    # addition
print(add_operation("23", "34"))    # concatenation