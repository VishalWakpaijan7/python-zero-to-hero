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

"""
random.choices() : method returns a list with the randomly selected element from the specified sequence.

You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

sequence |	Required. A sequence like a list, a tuple, a range of numbers etc.
weights  |	Optional. A list were you can weigh the possibility for each value.Default None
cum_weights | 	Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
                Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].
                Default None
k        |	Optional. An integer defining the length of the returned list
"""

# myList = ['apple', 'banana', 'cherry']
# print(random.choices(myList, weights=[10,5,15], k=8)) # not understood yet

"""
random.shuffle(): method takes a sequence, like a list, and reorganize the order of the items.
"""

# myList = [1,2,3,4,5]
# random.shuffle(myList) // return "None": this method change the original list, it does not return new list
# print(myList)

"""
random.sample(): method return a list with specified numbers of randomly selected items from a sequence
"""

# myList = ['apple','banana','orange']
# newList = random.sample(myList,k=2) # return a list with randomly selected items from myList to newList
# print(newList) # k is cannot be longer than provided sequence length

# OR

# print(random.sample(myList,k=2))

"""
radom.random() : method return random floating number between 0 to 1
"""

# print(random.random())

"""
radom.uniform() : method return random floating number between two specified numbers (both included)
"""

# print(random.uniform(1.5,5.5))

"""
 ##### TRIANGULAR ####

Syntax : random.triangular(low, high, mode)
Parameters :
low : the lower limit of the random number
high : the upper limit of the random number
mode : additional bias; low < mode < high
if the parameters are (10, 100, 20) then due to the bias, most of the random numbers generated will be closer to 10 as opposed to 100.
Returns : a random floating number

"""

# print(random.triangular(10,100,20))

# for i in range(10):
#     print(random.triangular(10,200,100))

"""
    random module methods used in "STATISTICS"
"""

"""
### BETAVARIATE ###

Syntax: random.betavariate() : Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
Beta distribution: 
The beta distribution is used to model continuous random variables whose range is between 0 and 1.
For example, in Bayesian analyses, the beta distribution is often used as a prior distribution of the parameter p 
(which is bounded between 0 and 1) of the binomial distribution 
(see, e.g., Novick and Jackson, 1974)
"""

# print(random.betavariate(1,10))

"""
#### EXPOVARIATE ####

Syntax: random.expovariate() : Returns a random float number based on the Exponential distribution (used in statistics)
Exponential distribution: 
In Probability theory and statistics, the exponential distribution is a continuous probability distribution that often concerns the amount of time until some specific event happens.
It is a process in which events happen continuously and independently at a constant average rate.

"""

# print(random.expovariate(10000.0))

"""
#### GAMMAVARIATE ###

Syntax : random.gammavariate(alpha, beta)
Parameters :
alpha : greater than 0
beta : greater than 0
Returns : a random gamma distribution floating number based on Gamma distribution (used in statistics)
"""

# print(random.gammavariate(100,1))

"""
 ######### PROBABILITY THEORY #########
"""

"""
### GAUSS ###

Syntax : random.gauss(mu, sigma)
Parameters :
mu : mean
sigma : standard deviation
Returns : a random gaussian distribution floating number  based on the Gaussian distribution (used in probability theories)
"""

# print(random.gauss(100,50))

"""
### LOGNORMVARIATE ####

Syntax : random.lognormvariate(mu, sigma)
Parameters :
mu : mean
sigma : standard deviation, greater than 0
Returns : a random log-normal distribution floating number based on a log-normal distribution (used in probability theories)

"""
# print(random.lognormvariate(0,0.25))

"""
### NORMALVARIATE ####

Syntax : random.normalvariate(mu, sigma)
Parameters :
mu : mean
sigma : standard deviation
Returns : a random normal distribution floating number based on a  normal distribution (used in probability theories)

"""

# print(random.normalvariate(100,50))

"""
#### PARETOVARIATE #### 
Syntax : random.paretovariate(alpha)
Parameter :
alpha : shape parameter
Returns : a random Pareto distribution floating number
"""

# print(random.paretovariate(5))

"""
    ## DIRECTIONAL STATISTICS
""" 

"""
### VONMISESVARIATE ####

Syntax : random.vonmisesvariate(mu, kappa)
Parameters :
mu : mean angle, expressed in radians between 0 and 2*pi
kappa : concentration parameter, greater than or equal to zero
Returns :  a random float number based on the von Mises distribution (used in directional statistics)

"""
# print(random.vonmisesvariate(0,4))


""" 
 ### STATISTICS ###
"""

"""
#### WEIBUllVARIATE ###

Syntax : random.weibullvariate(alpha, beta)
Parameters :
alpha : scale parameter
beta : shape parameter
Returns : a random Weibull distribution floating number

"""

# print(random.weibullvariate(1,1.5))