"""
* PYTHON SCOPE
* A variable is only available from inside the region it is created. This is called scope.
"""

# * Local Scope : A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# def myFunction():
#     x = 25 # * variable x in local scope
#     print(x)

# myFunction()

# * Function inside function

# def myFunc():
#     x = 225
#     def myInnerFunc():
#         print(x) # * Inner function have access to outer function variable
#     myInnerFunc()
# myFunc()

# * Global Scope: 
"""
* A variable created in the main body of the Python code is a global variable and belongs to the global scope.
* Global variables are available from within any scope, global and local.
"""

# x = 300 # global scope variable

# def myFunc():
#     print(x)

# myFunc()

# * Naming variables : 
"""
If you operate with the same variable name inside and outside of a function,
Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
"""

# x = 300

# def myFunc():
#     x = 200
#     print(x) # 200

# myFunc()

# * Global keyword :
"""
* If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
* The global keyword makes the variable global.
"""

# def myFunc():
#     global x
#     x = 300

# myFunc()
# print(x)

# x = 500
# def myFunc():
#     global x
#     x = 300

# myFunc()

# print(x)

# * Nonlocal Keyword:
"""
* The nonlocal keyword is used to work with variables inside nested functions.
* The nonlocal keyword makes the variable belong to the outer function.
"""

# def myFunc1():
#   x = "Jane"
#   def myFunc2():
#     nonlocal x
#     x = "hello"
#   myFunc2()
#   return x

# print(myFunc1())
