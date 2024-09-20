"""
*  PYTHON CLASSES AND OBJECTS

* Python is object oriented programming language.
* almost everything in python is an object, with its properties and methods.

A Classes is like object constructor, or a "blueprint" for creating objects/
"""

# * Create class

# class MyClass:
#     x = 5

# * Create Object

# p1 = MyClass()
# print(p1.x)

# * The __init__() Function
"""
* The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
* To understand the meaning of classes we have to understand the built-in __init__() function.
* All classes have a function called __init__(), which is always executed when the class is being initiated.
* Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
"""

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person('John',36)
# print(p1.name)
# print(p1.age)

# class Car:
#     def __init__(self,model,year,color):
#         self.model = model
#         self.year = year
#         self.color = color

# c1 = Car('BMW m1',2021,'white')
# print(c1.model,c1.year,c1.color)

# * The __str__() Function : 
"""
* The __str__() function controls what should be returned when the class object is represented as a string.
* If the __str__() function is not set, the string representation of the object is returned:
"""

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):                      # define __str__()
#         return f"{self.name}({self.age})"

# p1 = Person('Vishal',26)

# * The string representation of an object WITHOUT the __str__() function:
# print(p1) # * <__main__.Person object at 0x000001E5C26A62A0>

# The string representation of an object WITH the __str__() function:
# print(p1) # * return: Vishal(26)

# * Object Methods : Objects can also contain methods. Methods in objects are functions that belong to the object.

# class Car:
#     def __init__(self,model,year):
#         self.model = model
#         self.year = year

#     def carDetails(self):
#         print(f'I have {self.model} and it\' from year {self.year}')

# p1 = Car('Mustang GT9',1998)
# p1.carDetails()

# * The self Parameter: 
"""
* The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
* It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

class Person:
    def __init__(personObject,name,age):
        personObject.name = name
        personObject.age = age

    def getPersonDetails(person):
        print(f"Person name: {person.name} and he/she is {person.age}")

p1 = Person('Jane',25)

# p1.getPersonDetails()

# * Modify Object Properties

print("Before obj property modification:" ,p1.age)
p1.age = 23
print("After obj property modification:" ,p1.age)

# * Delete Object Properties

# del p1.age
# print(p1.age) #! AttributeError: 'Person' object has no attribute 'age'

# * Delete Objects

# del p1
# print(p1) # ! NameError: name 'p1' is not defined

# * The pass statement:
# * class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# class Person:
#     pass