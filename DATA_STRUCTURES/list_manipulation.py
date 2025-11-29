# list manipulation in PYTHON:

# Lists -> The list stores multiple datas, using [] or list()
# They are ordered, changeable, allow duplicates, modifiable
# These are mutable datatypes & heterogenous in nature

numbersList = [1,2,3,4,5,6]
charsList = ['a','e','i','o','u','b','c','f','d']

print(numbersList)
print(type(numbersList))
print(charsList)
print(type(charsList))

list1 = [5, 'low', 8.9, True, False]
list2 = ['$$', 89, True, 78.4]
print(list1, list2, sep='\n')


# list using range() function: 
# returns list of nums from (start, end - 1)
print(list(range(8)))
print(list(range(2,6)))

list3 = list(range(3,9,2))
print(list3)

# list replication and concatenation:
list4 = list3 * 3
print(list4)

list5 = list3 + [6,7,0]
print(list5)


# accessing elements of the lists using index, slicing:
list6 = [5, 'low', 8.9, True, False]
list7 = ['$$', 89, True, 78.4]

# modify specific item value
print(list6[2])
list6[2] = 7.65
print(list6[2])

# accessing range of item values
print(list7[1:3])
print(list7[:3])
print(list7[::-1])

list8 = [10, 11, 12, 13, 14, 15]
print(list8)
# modify range of the item values
# no. of old items & new items doesn't matter
list8[0:2] = ["Ten"]
print(list8)

print(dir(list1))

# List manipulation methods:
newList = ["flight", "van", "van", "Bullock", "train", "cycle"]
print(newList)
newList.append("cars")
print(newList)

newList.extend(["scooters", "bikes"])
print(newList)

newList.insert(2, "ship")
print(newList)

print(newList.index("van"))
print(newList.count("van"))

# removing elements from the list:
newList.remove("bikes")
print(newList)
# remove value at specific index / 
# last position (default)
newList.pop()
newList.pop(1)
print(newList)

# newList.clear()  # deletes list contents
# print(newList)

# del newList        # deletes list completely
# print(newList)

print(newList)
newList.sort(key=str.lower)
print(newList)

l1 = ['Bananas', 'Papayas', 'Cherries']
l2 = l1[:]

l1.append("Plums")
print(l1)
print(l2)

print(l1 and l2)
print(l1 or l2)

print('Papayas' in l2)
print('Bananas' not in l1)

matrix = [[1,2,3],[3,4,5],[4,5,6]]
print(matrix[1])
print(matrix[2][0:1])
print(matrix[1][1])


valuesList = [10, 20, 30, 40, 50, 60]

# # adding values to list using iteration:
# finalValues = []
# for num in valuesList:
#     finalValues.append(num * 2)
# print(finalValues)

# adding values to list using list comprehension:
finalValues = [(num * 2) for num in valuesList]
print(finalValues)

# filtering values to list using list comprehension:
names = ['anna','john','carrie','alpha','gord']
names_with_a = [all_items for all_items in names if 'a' in all_items]
print(names_with_a)

