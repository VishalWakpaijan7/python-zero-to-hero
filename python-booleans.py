""" 
    * PYTHON BOOLEANS
    * Boolean represent one of two values: True or False
"""

# print(10 < 9)
# print(10 > 9)
# print(10 == 9)

# * When you run condition in an if statement, python return True or False

"""
a = int(200)
b = int(100)
if a > b:
    print('a is greater than b')
else:
    print('b is greater than a')
"""

# * Evaluates values and variables
# * The bool() function allows you to evaluate any value, and give you True or False in return

# print(bool('hello')) # False
# print(bool('20')) # False
# print(bool('')) # False
# print(bool()) # False

# * Evaluates variable

# a = 'Hey'
# b = 25

# print(bool(a)) # True
# print(bool(b)) # False

"""
* Almost any value is evaluated to True if it has some sort of content.
* Any string is True, except empty strings.
* Any number is True, except 0.
* Any list, tuple, set, and dictionary are True, except empty ones.
"""

# print(bool(['test']))
# print(bool({'Test': 'Test'}))

""" 
    * In fact, there are not many values that evaluate to False,
    * except empty values, such as (), [], {}, "", the number 0, and the value None.
    * And of course the value False evaluates to False. 
"""

# print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))

""" 
    * One more value, or object in this case, evaluates to False,
    * and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""

# class myClass():
#     def __len__(self):
#         return 0

# myObj = myClass()
# print(bool(myObj))

""" 
* Functions can return boolean
"""

# def myFunction():
#     return True

# print(myFunction())

# You can execute code base based on the Boolean answer of the function

# def myFunction():
#     return False

# if myFunction():
#     print('Yes')
# else:
#     print('No')

""" 
* Python also has many built-in functions that return a boolean value,
* like the isinstance() function, which can be used to determine if an object is of a certain data type
"""

# x = '200'
# print(isinstance(x, str))