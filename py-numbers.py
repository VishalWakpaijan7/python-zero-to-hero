## PYTHON NUMBERS

# There are three numeric types in python

# int : Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# x = 1
# y = 35656222554887711
# z = -3255522

# float : Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# x = 1.10
# y = 1.0
# z = -35.59
# Float can also be scientific numbers with an "e" to indicate the power of 10.
# x = 35e3
# y = 12E4
# z = -87.7e100

# complex : Complex numbers are written with a "j" as the imaginary part:
# x = 3+5j
# y = 5j
# z = -5j

# x = 1 # int
# print(x)

# y = 2.8 # float
# print(y)

# z = 1j # complex
# print(z)

# Verify type of variable using type() function

# print(type(x),type(y),type(z)) # print = <class 'int'> <class 'float'> <class 'complex'>

## TYPE CONVERSION

# You can convert from one type to another with the int(), float(), and complex() methods:

# x = 1
# y = 2.8
# z = 5j

# # converting int to float
# a = float(x)
# print('VALUE:', a , 'TYPE:', type(a))

# # converting to float to int
# b = int(y)
# print('VALUE:', b , 'TYPE:', type(b)) # removed values after decimal point

# # converting int to complex

# c = complex(x)
# print('VALUE:', c , 'TYPE:', type(c))

# Note: You cannot convert complex numbers into another number type.

## RANDOM NUMBER 

"""
Python does not have a random() function to make random number but python has a built-in module called random 
that can be used to make random numbers:

"""

import random

## The random module has a set of methods:
"""
 random.seed() # Initialize the random number generator
"""
# print(random.random())
# print(random.randrange(1,10))

"""
print(random.getstate()) # Returns the current internal state of the random number generator
"""

""" 
random.setState example: 
The setstate() method is used to restore the state of the random number generator back to the specified state

"""
# print(random.random()) # printing random number
# state = random.getstate() # capture the state
# print(random.random()) # print another random number
# random.setstate(state) # restoring the state
# print(random.random())

"""
random.getrandbits() : The getrandbits() method returns an integer in the specified size (in bits).
"""
# print(random.getrandbits(16))

"""
random.randrange() : The randrange() method returns a randomly selected element from the specified range.
"""
# print(random.randrange(1,100)) # return random integer between 1 to 100

"""
random.randint() : The randint() method returns an integer number selected element from the specified range. 
Note: This method is an alias for randrange(start, stop+1).
"""
# print(random.randint(1,10)) # return random number between 1,10 (both included)

"""
random.choice() : The choice() method returns a randomly selected element from the specified sequence.
The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
"""

# myList = ['apple','banana','cherry']
# print(random.choice(myList))

# userName = 'vishal wakpaijan'
# print(random.choice(userName))

