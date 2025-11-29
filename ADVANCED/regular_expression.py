# Regular Expression (RegEx) in PYTHON:

# a RegEx is sequence of chars that forms the search patterns to locate the chars/files/foldersj

import re

text = "Hello I am Python Language Interpreter"
pattern = 'e'

# findall(): returns list containing all matches of patterns in string
x = re.findall(pattern, text)
print(x)

# search()
x = re.search(pattern, text)
print(x)
print(x.span())
print(x.group())
print(x.string)

# split()
x = re.split(pattern, text, 2)
print(x)

# sub()
x = re.sub(pattern, '**', text, 1)
print(x)



# quantifiers (meta-charecters) in Regular Expressions in PYTHON:
# meta-charecters -> special set of chars that have special meanings

# Quantifiers are used to specify the number of times a particular character, 
# group of characters, or a metacharacter should be matched in the given pattern

# import re

# # * -> char occurs any number of times including zero
# # + -> char occurs any number of times excluding zero
# # ? -> char occurs exactly 0 or 1 time
# # {n} -> char occurs n number of times
# # . -> any char which had occurred
# # [char-char] -> set of chars from start to end occurred
# # ^, $ -> any char start(^) with (or) ends($) with
# # |, & -> charecter occurred based on condition given

# text = "Hello I am Python Language Interpreterzxn"
# pattern = '^H...o'

# x = re.findall(pattern, text)
# print(x)



# Special Chars and Special Sequences in Regular Expressions in PYTHON:

# To improve search patterns by making to find specific chars or set of special chars easily
# using Special Sequences like : '/' (back-slash) inside r'' (raw-string) and 
# using Special Characters like: "*, !, $,..., numbers, letters" insisde [] (set-braces)
# to define unique meaning thus preventing ambiguity.

# import re

# text = "Hello I am ** Python 15 02 Language Interpreter"
# pattern = r'\AHello' # or else like '[*]'

# x = re.findall(pattern, text)
# print(x)

# if x:
#     print("There is a match..")
# else:
#     print("No match found..")

# # print(''.join(x))