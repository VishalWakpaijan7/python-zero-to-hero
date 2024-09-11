"""
* PYTHON OPERATORS
Operators are used to perform operations on variables and values.

Python divide the operators in different groups following:
 1.Arithmetic operators 
 2.Assignment operators
 3.Comparison operators
 4.Logical operators
 5.Identity operators
 6.Membership operators
 7.Bitwise operators
"""

# * Arithmetic Operators ( Arithmetic operators are used with numeric values to perform common mathematical operations )

# * Addition
# print(2+2)

# * Subtraction
# print(100 - 57)

# * Multiplication
# print(10 * 50)

# * Division
# print(75 / 5)

# * Comparison operators ( Comparison operators are used to compare two values )

# x = 80
# y = 50

# print(x == y) # * Equals
# print(x != y) # * Not Equal
# print(x > y) # * Greater than
# print(x < y) # * Less than
# print(x >= y) # * Greater than or equals to 
# print(x <= y) # * Less than or equals to 

# * Logical operators ( Logical operators are used to combine conditional statements )

# x = 5
# print(x > 3 and x < 10) # * "and" : Returns True if both statements are true
# print(x > 3 or x < 4) # * "and" : Returns True if one of the statements is true
# print(not(x < 8 and x > 4 )) # * "and" : Reverse the result, returns False if the result is true

# * Identity operators ( Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location )

# x = ['apple','banana']
# y = ['apple','banana']
# z = x

# * "is" : Returns True if both variables are the same object

# print(x is z) # * returns True because z is the same object as x
# print(x is y) # * returns False because x is not the same object as y, even if they have the same content
# print(x == y) # * return True because x is equal to y if we use == (Equal) comparison operator

# * "is not" : Returns True if both variables are not the same object

# print(x is not z) # * returns False because z is the same object as x
# print(x is not y) # * returns True because x is not the same object as y, even if they have the same content
# print(x != y) # *  return False because x is equal to y if we use != (Not equal) comparison operator

# * Membership operators ( Membership operators are used to test if a sequence is presented in an object )

# * "in" : Returns True if a sequence with the specified value is present in the object
# print('banana' in x) # * returns True because a sequence with the value "banana" is in the list

# * "not in" : Returns True if a sequence with the specified value is not present in the object
# print('orange' not in x) # * returns True because a sequence with the value "orange" is not in the list

