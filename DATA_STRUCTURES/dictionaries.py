# dictionaries in PYTHON:
# the dictionaries are ordered, changeable (mutable)
# allows duplicate values, but not same keys

# creating a dictionary: using {key:value} pair
contact1 = {
    'Name':"Preveen",
    'Phone.no':9488960369,
    'Place':"Madurai",
    'Pincode': 625107,   
}

# accessing the items of the dictionary (manipulation)
print(contact1)
print(type(contact1))
print(len(contact1))
# values are accessed by their keys, not indexes
print(contact1.get('Name'))
print(contact1['Phone.no'])
# print all the keys, values, items of dictionary
# print(contact1.values())
# print(contact1.keys())
print(contact1.items())


# creating a dictionary from a list using dict()
contact2_list = [('Name',"Pranesh"),('Phone.no',9434964569),
                  ('Place',"Viraganur"),('Pincode', 625009)]
contact2 = dict(contact2_list)
print(contact2)


# creating a dictionary list of keys, list of values using zip()
# zip() -> combines two lists into pairs of tuples, by mapping the elements of
# those list values correspondingly as follows for conversion into dictionary
list_keys = ['Name', 'Phone.no', 'Place', 'Pincode']
list_values = ["Kiran", 7878787878, "Thirupuvanam"]
contact3 = dict(zip(list_keys, list_values))
print(contact3)

# updating values in dictionary
contact3['Pincode'] = 630672
print(contact3)

# some boolean checking methods
print(all(contact3))    # returns true
print(any(contact3))    # returns true

# deleting values from dictionary using keys
contact3.pop('Place')
print(contact3)
contact3.popitem()
print(contact3)
del contact3['Phone.no']
print(contact3)
contact3.clear()
print(contact3)

print(all(contact3))    # returns true
print(any(contact3))    # returns false

import ast

# creating a dictionary from string using ast.evalutae_str()
# ast is python library -> assymetric trees
contact4_str = "{'Name':'Rajaguru','Phone.no':9488888369," \
"'Place':'Madurai','Pincode': 625009}"
contact4 = dict(ast.literal_eval(contact4_str))
print(contact4)


print(contact1.items())

# looping items of dictionary using for loop:
for key, value in contact1.items():
    print(f"{key = } and {value = }") 

# sorting items of dictionary based on keys, values

# sorting dict based on keys:
sort_contact1 = dict(sorted(contact1.items()))
print(sort_contact1)

# # sorting dict based on values:
# sort_contact1 = dict(sorted(contact1.items(), key=lambda item:item[1]))
# print(sort_contact1)

