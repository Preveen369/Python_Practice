# Strings manipulation in PYTHON:

# Strings -> a datatype where the set of characters are 
# surrounded by single/double/triple quotes or else use str()
# These are immutable datatypes & homogenous in nature

name = "My name is Preveen"
age = 22

print(name.capitalize())
print(name.upper())
print(name.lower())
print(len(name))

print(name.encode())
print("Hello, my name is {}!!".format(name))
print("I am {} years old".format(age))


process1 = "Synchronization"
process2 = 'Multithreading'

print(process1, process2, sep='\n')
print(type(process1), type(process2), sep='\n')


multiline = '''This is a multiline string. So that generally,
it is very easier to append the characters!'''

print(multiline)
print(type(multiline))
print(len(multiline))
print(dir(multiline))


sentence = "This is a powerful speech"
print(len(sentence))            # length of sentence 
print(len(sentence.split()))    # length of each word


# string multiplication
string1 = "Repeat"
string2 = string1 * 2
print(string2)

# string concatenation
string3 = "Starting "
string4 = "Stopping"
resultStr = string3 + string4
print(resultStr)

# membership operations in strings
exampleStr = "My favorite car is FERRARI"
print(exampleStr)
print("FERRARI" in exampleStr)
print("DUCATI" not in exampleStr)

# accessing the string characters
print(exampleStr[3])
print(exampleStr[-4])

# String slicing in Python
print(exampleStr[2:13])
print(exampleStr[:])
print(exampleStr[7:])
print(exampleStr[:9])
print(exampleStr[::2])

reverse_string = exampleStr[::-1]
print(reverse_string)

# strings case modification
unique_name = "UNICORN STARTUP STAR COMPANY"
print(unique_name.capitalize())
print(unique_name.title())
print(unique_name.lower())
print(unique_name.casefold())
print(unique_name.upper())
print(unique_name.swapcase())

# is true? String methods 
print(unique_name.isalnum())
print(unique_name.isalpha())
print(unique_name.isdigit())
print(unique_name.isspace())
print(unique_name.isupper())

# find() string method:
print(unique_name.find("COMPANY"))
print(unique_name.find("STAR", 10))

# index() string method:
print(unique_name.index("COMPANY"))
print(unique_name.index("STAR", 10))

# remove/replace spaces/characters from a string
exampleString = "  a  beautiful  lawn in the dawn   "
print(exampleString.replace("  ", "**"))
print(exampleString.strip())

exampleWords = exampleString.split()
print(exampleWords)
print(" ".join(exampleWords))

# count the number of occurrences in string
print(exampleString.count('awn'))
print(exampleString.count('i'))

newString = "beatiful dawn"
print(sorted(newString.strip()))
newString += " over daytime"
print(newString)
print(newString.partition(" "))
print("98".zfill(4))


ordinal_val = ord('a')
print(ordinal_val)
ascii_char = chr(97)
print(ascii_char)

