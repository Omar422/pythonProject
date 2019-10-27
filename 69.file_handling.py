# 69 . File Handling In Python

"""
# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode
# There are four different methods (modes) for opening a file:
    1/ "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
    2/ "a" - Append - Opens a file for appending, creates the file if it does not exist.
    3/ "w" - Write - Opens a file for writing, creates the file if it does not exist.
    4/ "x" - Create - Creates the specified file, returns an error if the file exists.
# In addition, you can specify if the file should be handled as binary or text mode
    "t" - Text - Default value. Text mode "b" - Binary - Binary mode (e.g. images)
# To open the file, use the built-in open() function.The open() function returns a file object, which
    has a read() method for reading the content of the file
# By default the read() method returns the whole text, but you can also specify how many
    characters you want to return.
# Note: You should always close your files, in some cases, due to buffering, changes made to a
    file may not show until you close the file.

## Writing:
# To write to an existing file, you must add a parameter to the open() function.
    # "a" - Append - will append to the end of the file
    # "w" - Write - will overwrite any existing content

## Delete File
# To delete a file, you must import the OS module, and run its os.remove() function
# To delete an entire folder, use the os.rmdir() method.
# Note: You can only remove empty folders.
"""

import os

f = open('test.txt')
print("using read():\n")
#print(f.read())
print(f.read(6))
f.close()

print("------------\nusing readline():\n")
f = open('test.txt')
print(f.readline())
print(f.readline())
f.close()

print("------------\nusing for:\n")
for x in open('test.txt'):
    print(x)
f.close()


# Writing
f = open('test2.txt')
print("------------\nMain Content: "+f.read())

f = open('test2.txt', 'a')
f.write('Added Content')
f.close()

f = open('test2.txt')
print("\nAfter Append: "+f.read())











f = open('test3.txt')
print("------------\nMain Content: "+f.read())

f = open('test3.txt', 'w')
f.write('replac content \'w\'')
f.close()

f = open('test3.txt')
print("\nContent: "+f.read())
f.close()

f = open('newfile_Python.txt', 'x') # create the file
f.close()
os.remove('newfile_Python.txt') # remove the file

if os.path.exists('newfile_Python'):
    os.remove('newfile_Python.txt') # doesn't exist
else:
    print("Doesn't Exist")

os.rmdir('folder')
