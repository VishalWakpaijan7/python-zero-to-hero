"""
* PYTHON FUNCTIONS
"""

# * creating py function

# def my_function():
#     print('Hello Python!')

# my_function()

# * arguments 

# def displayName(name):
#     print('Hey {fname}'.format(fname=name))

# displayName('vishal')

# def userDetails(name,age):
#     print('Hey my name is {n} and i am {a}'.format(n=name,a=age))
# userDetails('vishal',25,'test@gmail.com') # ! throw error if we pass extra arguments than expected

# * Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly

# def my_function(*kids):
#     print("Hello,"+ kids[2])

# my_function('Sachin','Vishal','Pratik')

# * Keyword arguments : You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

# def my_function(child3,child1,child2):
#     print('The youngest child is:' + child3)

# my_function(child1='sachin',child2='pratik',child3='vishal')

# * Arbitrary Keyword Arguments, **kwargs
# * If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# def my_function(**kid):
#     print('His last name is: ' + kid['lname'])

# my_function(fname='vishal',lname='wakpaijan')

# * Default parameter value

# def my_function(country = 'India'):
#     print('I am from ' + country)

# my_function('USA')
# my_function() # ? when we call function without argument it used default

# * Passing a List as an Argument :
"""
* You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function
"""

# def my_function(food):
#     for x in food:
#         print(x)

# my_function(['apple','banana','orange'])

# * Return values : To let a function return a value, use the return statement

# def my_function(n):
#     return 5 * n

# print(my_function(5))

# * The pass statement : function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# def my_function():
#     pass

# * Positional-Only Arguments: 
"""
*You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
*To specify that a function can have only positional arguments, add , / after the arguments:
"""

# def my_function(x,/):
#     print(x)

# my_function(x=5) # ! TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x'

# * Keyword-Only Arguments: To specify that a function can have only keyword arguments, add *, before the arguments:

# def my_function(*,x,y):
    # print(x + y)

# my_function(x=5,y=6)
# my_function(5,6) # ! TypeError: my_function() takes 0 positional arguments but 2 were given

# * Combine Positional-Only and Keyword-Only

# def my_function(a,b,/,*,c,d):
#     print(a + b + c + d)
# my_function(5,4,c=5,d=8)

# * Recursion:
"""
* Python also accepts function recursion, which means a defined function can call itself.
* Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
"""

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# tri_recursion(6)