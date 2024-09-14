"""
    * PYTHON TUPLES :
    Tuples are used to store multiple items in a single variable.
    Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
    A tuple is a collection which is ordered and unchangeable.
    Tuples are written with round brackets
"""

# * Creating tuple

thisTuple = ('apple','banana','orange')
# print(thisTuple)

# * Tuple Items
# * Tuple items are ordered, unchangeable, and allow duplicate values.
# * Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# * Ordered
# * When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# * Unchangeable
# * Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# * Allow Duplicates
# * Since tuples are indexed, they can have items with the same value:

# * len method to find tuple length

# print(len(thisTuple)) # * 3

# * Create tuple with one item : To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple

# singleItemTuple = ('Apple',)
# singleItemTuple = ('Apple') # return <class str> type
# print(type(singleItemTuple))

# * Tuple constructor : we can make tuple with tuple() constructor

# tupleWithConstructor = tuple(('Apple','Banana','Orange')) # note the double round-brackets
# print(tupleWithConstructor,type(tupleWithConstructor))

#  ? ######################## Access Tuples ########################

