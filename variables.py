## Python have no command for declaring variables

# x = 5
# y = 'Vishal'

# print(x)
# print(y)

# x = 'Wakpaijan'

# print(y,x)

## Casting allow us to specify the data-types

# z = str(5)
# m = int(5)
# f = float(3)

# print(z)
# print(m)
# print(f)

## Variables naming convection

# A variable name must start with a letter or the underscore character eg. firstName, _userList
# A variable name cannot start with a number 
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ) eg. first_name, last-name 
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

## Python variables support camel-case, pascal-case and snack-case

## Many values to multiple variables

# x,y,z = 'Orange','Banana','Apple' # Make sure the number of variables matches the number of values, or else will get an error.

# print(x)
# print(y)
# print(z)

## One value to multiple variables

# x = y = z = 'Banana'

# print(x)
# print(y)
# print(z)

##  Unpacking Collection : If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# fruits = ['apple', 'banana', 'cherry']
# x,y,z = fruits # Make sure the number of variables matches the number of list values, or else will get an error.

# print(x)
# print(y)
# print(z)

## Output Variables

# x = str('Python is awesome')
# print(x) # print() function is often used to output variables

## We can output multiple variables in print using comma , or + mathematical operator

# x = str('Vishal')
# y = str('wakpaijan')

# z = int(24)

# print(x,y,"is",z,'years old!') # Vishal Wakpaijan is 24 years old!

# x = 'Python '
# y = 'is '
# z = 'awesome'

# print(x + y + z) # print dont trim the string by default : Python is awesome

# x = 5
# y = 'test'

# print(x,y) # result 5 test don't throw error
# print(x + y) # throw error cannot combine string to number

## Python Global Variables

# Variables created outside the function are all global variables as above eg.
# Global variables can be used by everyone, both inside of function and outside

# x = 'awesome'

# def myFunction():
#     print("Python is " + x)

# myFunction()

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value
"""

"""
def myFunc():
  x = "fantastic"
  print("Python is " + x)

myFunc()
print("Python is " + x)
"""

## The Global Keyword

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create global variable inside the function we can use global keyword
"""

"""
def myFunc():
    global x
    x = str('Fantastic')
    y = int(25)
    print('My age is ', y)
myFunc()

print('Python is ' + x)
"""

# use global keyword if you want to change global variable inside function

"""
x = 'awesome'
print("Before:", x)
def myFunc():
    global x
    x = 'fantastic'
    print("Inside myFunc: Python is", x)

myFunc()
print("After:", x)
"""