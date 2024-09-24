"""
* PYTHON TRY EXCEPT
* The try block lets you test a block of code for errors.
* The except block lets you handle the error.
* The else block lets you execute code when there is no error.
* The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# * Exception Handling

# try:
#     print(x)
# except:
#     print('hello exception occurred')

# * Many exception: You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error

# try:
#     # x = 'test' + 21
#     print(x)
# except NameError:
#     print('Variable x is not define')
# except:print('Something else went wrong')


# * Else: You can use the else keyword to define a block of code to be executed if no errors were raised:

# try:print('Hello')
# except: print('Something went wrong')
# else:print('Nothing went wrong')

# * finally:  finally block, if specified, will be executed regardless if the try block raises an error or not.

# try:print(x)
# except:print('Something went wrong')
# finally:print('The "try except" is finished')

# * file opening example

# try:
#     f = open("demoFile.txt")
#     try: f.write('Hello World') 
#     except:print('something went wrong when writing to the file')
#     finally:f.close()
# except:print('something went wrong when opening the file')

# * Raise an exception

# x = -1

# if x < 0:
#     raise Exception('Sorry, no numbers below zero')

# x = 'hello'
# if not type(x) is int:
#     raise TypeError('Only integers are allowed')

# x = 20
# if not type(x) is str:
#     raise TypeError('Only str are allowed')
