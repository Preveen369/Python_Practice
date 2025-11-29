# set manipulation in PYTHON
# sets: unordered, unchangeable collection of elements
# doesn't allow duplicate values in it

set1 = {10, 20, 30, 40, 50, 60}
set2 = {20, 30, 40, 50}

print(set1)
print(set2)

# adding elements in set:
print(set1)
set1.add(70)
print(set1)

# updating elements between sets:
print(set2)
set2.update(set1)
print(set2)

print(set1)
set1.discard(10)    # doesn't raise any error
set1.remove(20)     # raises err when value not present
print(set1)

print(set2)     
set2.pop()      # deletes front element from set
print(set2)

set3 = {30, 31, 32, 33, 41, 40}
set4 = {30, 31, 32, 33, 34, 35, 36}

print(set3)
print(set4)

print(set3.union(set4))
print(set3.intersection(set4))
print(set3.symmetric_difference(set4))

# set differences:
print(set3 - set4)
print(set4 - set3)

