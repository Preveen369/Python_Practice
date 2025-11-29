# tuple manipulation in PYTHON:
# they are ordered, immutable, can't be modified
# represented using paranthesis ()

t1 = (10, 20, 30, 40, 50)
t2 = (True, False, 'Vijay', "Ramesh", 56.0)

print(t1)
print(t2)
print(len(t1), len(t2))

# print(t1, t2, sep=' ')

print(type(t1))
print(type(t2))

t3 = ('45',)
print(t3)
print(type(t3))
print(len(t3))

# in tuple, once items stored they can't be 
# directly modified, but can be accessed using 
# indexing / slicing / loops

# accessing tuple elements:
tuple1 = (10, 20, 30, 40, 50)
print(tuple1)
print(tuple1[1])
print(tuple1[-2])
print(tuple1[:])
print(tuple1[1:4])
print(tuple1[::2])
print(tuple1[::-1])

# indirectly modifying elements of tuple:
tuple2 = (True, False, 'Vijay', "Ramesh", 56.0)
print(tuple2)

list_tup = list(tuple2)
# print(list_tup)
list_tup[0] = False
# print(list_tup)

tuple2 = tuple(list_tup)
print(tuple2)


# packing and unpacking tuple values:
# packing -> putting all values together in tuple and assigning to variable
# unpacking -> extracting all values from tuple and assigning to each variable
# number of values to be packed & unpacked must be the same, else
# * operator could be used to store the remaining packed values (as list type)

t3 = (10, 20, 30, 40, 50, 80)   # packing a tuple
a, b, c, *d, e = t3  # unpacking a tuple

print(t3)
print(a, b, c, d, e, sep=" ")

# tuple manipulation methods:
t4 = (11, 12, 13, 45.2, 45.3, 45.4)
# print(dir(t4))
print(len(t4))
print(t4.count(12))
print(t4.index(11))

# Inserting elements in tuple:
# at starting or ending postion -> tuple concatenation
t5 = (11, 12, 13)
t5 = (10,) + t5 + (14, 15)
print(t5)

# inserting element at index position -> using lists
t6 = (23, 26, 27, 28)
print(t6)
list_tup1 = list(t6)
list_tup1.insert(1, (24, 25))   # adding nested tuple
# print(list_tup1)
t6 = tuple(list_tup1)
print(t6)

# sorting the tuple elements:
t7 = (43, 26, 58, 10, 27, 35)
print(sorted(t7))   # returns sorted list
print(t7)   # no changes
