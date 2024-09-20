"""
* PYTHON LAMBDA 
* A lambda function is a small anonymous function.
* A lambda function can take any number of arguments, but can have only one expression
"""

# x = lambda a : a + 10
# print(x(10))

# x = lambda a,b,c : (a * b) + c
# print(x(10,10,5))

# * Why use lambda functions ? : The power of lambda is better shown when you use them as an anonymous function inside another function.

# def my_function(n):
#     return lambda a : a * n

# myDoubler = my_function(2)
# myTriple = my_function(3)
# print(myDoubler(5))
# print(myTriple(5))

# * Use lambda functions when an anonymous function is required for a short period of time.