# ==========================
# ARITHMETIC OPERATORS
# --------------------------
# Perform basic mathematical operations.
# +   Addition
# -   Subtraction
# *   Multiplication
# /   True division (returns float)
# //  Floor division (returns int)
# %   Modulus (remainder)
# **  Exponentiation
# ==========================

# arithmethic operations
num1 = 10
num2 = 20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2) # Floor division
print(num1%num2) # Modulus
print(num1**3) # Exponentiation

# ==========================
# COMPARISON (RELATIONAL) OPERATORS
# --------------------------
# Compare two values and return a boolean result.
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# ==========================

# comparison operations
num1 = 89
num2 = 45
print(num1 == num2) 
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# ==========================
# LOGICAL OPERATORS
# --------------------------
# Combine or invert boolean expressions.
# and  True if both operands are True
# or   True if at least one operand is True
# not  Inverts the boolean value
# ==========================

# logical operations
expression = not((10 > 30) and (20 < 30) or (30 == 30))
print(expression) 

# ==========================
# ASSIGNMENT OPERATORS
# --------------------------
# Assign values to variables while optionally performing an operation.
# =   Simple assignment
# +=  Add and assign
# -=  Subtract and assign
# *=  Multiply and assign
# /=  Divide and assign
# //= Floor divide and assign
# %=  Modulus and assign
# **= Exponentiate and assign
# ==========================

# assignment operations
num = 60
num **= 2
print(num)

# ==========================
# BITWISE OPERATORS
# --------------------------
# Act on individual bits of integers.
# &   Bitwise AND
# |   Bitwise OR
# ^   Bitwise XOR
# ~   Bitwise NOT (one’s complement)
# <<  Left shift
# >>  Right shift
# ==========================

num = 10
# Bitwise operations
print(num & 1011)  # Bitwise AND
print(num | 1011)  # Bitwise OR    
print(~num) # Bitwise NOT (one's complement)

print(num >> 1)
print(num << 1)

# ==========================
# IDENTITY OPERATORS
# --------------------------
# Check if two variables point to the same object in memory.
# is     True if both variables reference the same object
# is not True if variables reference different objects
# ==========================

num3 = [45]
# num4 = [45]
num4 = num3
print(num3 is num4)

# ==========================
# MEMBERSHIP OPERATORS
# --------------------------
# Test whether a value is found within a sequence or collection.
# in     True if value is found
# not in True if value is not found
# ==========================

num3 = [45, 46, 47]
print(46 in num3)
print(48 not in num3)