# pickle statements and sequential file access in PYTHON

# Pickling: it is a concept which consists of serialization/de-serialization, 
# which is mainly used for converting the python objects to byte-streams
# for storing them in binary files / databases (DB's) and vice-versa.

# load() method -> to load data from binary file (de-serialization)
# dump() method -> to dump data to the binary file (serialization)

# Working with Binary Files: To open a file in binary format, add 'b' to the 
# mode parameter. Hence the "rb" mode opens the file in binary format for
# reading, while the "wb" mode opens the file in binary format for writing.
# Unlike text files, binary files are not human-readable. 
# When opened using any text editor, the data is unrecognizable.

import pickle

result = ["word", "words", "world", "worlds"]
print(type(result))

# # serialization
# with open("pickle_file.bin", "wb") as f:
#     pickle.dump(result, f)

# de-serialization
with open("pickle_file.bin", "rb") as f:
    content = pickle.load(f)

print(content)
print(type(content))

# The seek() and tell() Methods - file sequential accessing: 
# The tell() function is used to determine the current position of the file pointer, 
# The seek() function is used to move the file pointer to specified position of file.

with open("newfile_dup.txt") as f:
    # f.seek(56)
    print(f.tell()) 
    print(f.read())
    print(f.tell())
