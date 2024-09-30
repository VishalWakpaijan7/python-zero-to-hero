"""
PYTHON FILE OPEN
* File handling is an important part of any web application.
* Python has several functions for creating, reading, updating, and deleting files.
"""

# * File handling
"""
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

# f = open('demoFile.txt','r')

"""
* Python file open
* Open file on the server
"""

# * open() : The open() function returns a file object, which has a read() method for reading the content of the file

# f = open('demoFile.txt','r')
# print(f.read())

# * Read only part of the file

# f = open('demoFile.txt', 'r')
# print(f.read(5))

# * Write to an existing file

"""
* "a" - Append - will append to the end of the file
* "w" - Write - will overwrite any existing content
"""

# f = open('demoFile.txt','a')
# f.write('\nMy name is vishal wakpaijan')
# f.close()

# f = open('demoFile.txt','w')
# f.write('I have deleted the content')
# f.close()

# f = open('demoFile.txt','r')
# print(f.read())


# * Create new file 
"""
To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""

# f = open('demoFile2.txt','x')
# f = open('demoFile.txt', 'x') # file exist error

# * Delete a file :  to delete a file, you must import the os module, and run its os.remove() function:

import os

# * Delete file
# os.remove('demoFile2.txt') # ! if file not exist throw error

# * Check file exists
# if os.path.exists('demoFile.txt'):
#     os.remove('demoFile.txt')
# else: print('File does not exist!')

# # * Delete empty folder
# os.rmdir('testing')