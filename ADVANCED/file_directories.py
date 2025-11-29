# file directory handling and zipping in PYTHON:

# zip() function in python:
# used to combine the lists (contents) by mapping corresponding values
# contents can be unzipped using type-casting or by putting * [asterisk]
list_keys = ['Name', 'Phone.no', 'Place']
list_values = ["Kiran", 7878787878, "Thirupuvanam"]
contacts = zip(list_keys, list_values)
print(*contacts)    # returns contents after unzipped
print(contacts)    # returns the zip iterator object


# zipping of files in python:
# In python, the various files can be zipped into a zip file
# by using the "zipfile" module

import zipfile

# zipping the zip file:   [compress the content]
# with zipfile.ZipFile('python_files.zip', 'w') as archive:
#     archive.write('newfile.txt')
#     archive.write('newfiles.txt')
#     archive.write('newfile_dup.txt')

# unzipping the zip file: [extract the content]
# with zipfile.ZipFile('python_files.zip', 'r') as archive:
#     archive.extractall()


# file directories handling using os module:
# import os

# os.mkdir("new_folder")    -> to create new directory if not exists
# print(os.path.exists("new_folder"))   -> check if directory exists
# print(os.getcwd())    -> get the current working directory path
# os.chdir("../BASICS") -> change the current working directory
# print(os.getcwd())
# os.rmdir("new_folder")    -> remove the working directory
# os.remove("dummy.txt")    -> remove the file (single file)

# files = ['newfile.txt', 'newfiles.txt', 'newfile_dup.txt']
# for each_file in files:   -> remove the files (batches)
#     os.remove(each_file)
