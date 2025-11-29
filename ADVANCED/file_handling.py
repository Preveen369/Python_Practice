# file handling in PYTHON

# used to read, write, append and create the text/binary files
# open(filename with extension, file mode)
# r -> read(default); w -> write
# a -> append; x -> create

# close() method is used to make file changes permanent and safer
# if with statement used, file closes automatically, after operation

# read(), readlines() -> used to read text from files created
# in r mode, if file doesn't exist it raises error

# write(), writelines() -> used to overwrite text in files
# in w, a mode, if file doesn't exist it creates the file
# in w mode, the text gets overwritten, if file exists
# in a mode, the text gets appended to nextline, if file exists
# in x mode, the error is raised, if the file exists

# file write operation
f = open("newfile.txt","w")
f.write("\nThis is a text written to newfile")
f.close()

# file append operation
f = open("newfile.txt","a")
f.write("\nThis is a text appended to newfile")
f.close()

# file creation operation
try:
    with open("newfile.txt", "x") as f:
        f.write("newfile.txt created")
except FileExistsError:
    print("the file already exist!!")

# file reading operation
try:
    with open("newfile_dup.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("the file does not exist!!")
