"""
* Python Inheritance:
* Inheritance allows us to define a class that inherit all the methods and property from another class.
* Parent class is the class being inherited from, also called base class
* Chile class is the class that inherits from another class, also called derived class
"""

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def printName(person):
        print(f"{person.fname} {person.lname}")

# class Student(Person):
#     pass

# * Note using pass keyword when you do not want to add any other property or method to the class/

# std1 = Student('Vishal','Wakpaijan')

# std1.printName()

# class Student(Person):
#     def __init__(self, fname, lname, year): # * The child's __init__() function overrides the inheritance of the parent's __init__() function
#         super().__init__(fname,lname) # * super() function that will make the child class inherit all the methods and properties from its parent
#         self.graduationYear = year

#     def welcome(student):
#         print(f'Welcome,{student.fname} {student.lname} to the class of: {student.graduationYear}')

# x = Student('sachin','wakpaijan',2019)
# x.welcome()

# * If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.