# import mymodule
# import mymodule as mx
# import platform
# from mymodule import person1

# mymodule.greeting(mymodule.person1['name'])

# * Re-naming a Module: You can create an alias when you import a module, by using the as keyword


# a = mx.person1['name']
# print(a)

# * Built-in Modules : There are several built-in modules in Python, which you can import whenever you like.

# x = platform.system()
# print(x)
# print(platform.processor())

# * Using the dir() Function : There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# x = dir(platform)
# print(x)

# x = dir(mx)
# print(x)

# * Import from module : You can choose to import only parts from a module, by using the from keyword.
# print(person1['name'])