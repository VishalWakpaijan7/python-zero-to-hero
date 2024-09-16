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

# * You can access tuple items by referring to the index number, inside square brackets

# print(thisTuple[0]) # * return: apple

# * Ranges of indexes : You can specify a range of indexes by specifying where to start and where to end the range.
# * When specifying a range, the return value will be a new tuple with the specified items

# print(thisTuple[1:2]) # * return ("banana",)
# * The search will start at index 1 (included) and end at index 2 (not included)

# * Range of negative indexes
# * Specify negative indexes if you want to start the search from the end of the tuple

# print(thisTuple[-3:-1]) # * ('apple', 'banana')

# * Check if items exists

# if 'apple' in thisTuple:
#     print('Yes, apple is in the fruits tuples')

# ? ############### Update tuples ###############

# *Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# *But there are some workarounds

# * Change | add tuples values

# carsList = ['bwm','mercedes','fiat','ford']
# x = list(carsList)
# x[2] = 'toyota' # * to Change
# x.append('toyota') # * to Add
# print(x)
# carsList = tuple(x)
# print(type(carsList), carsList)

# * Add tuple to tuple

# x = ('toyota',)
# carsList += x
# print(carsList)

# * Remove items : Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items

# x = list(carsList)
# x.remove('fiat')
# print(x)

# * delete tuple completely

# del carsList
# print(carsList) # ! this will raise an error because the tuple no longer exists

# ? ########## Unpacking tuple #############

# * In python, we are also allowed to extract the values back into variables. This is called "unpacking"

# (green,yellow,red) = thisTuple
# print(green,yellow,red)

# * The number of variables must match the number of values in the tuple, if not,
# * you must use an asterisk to collect the remaining values as a list.

# (green,yellow,*red) = thisTuple
# print(green,yellow,red) # *return: apple banana ['orange']

# * If the asterisk is added to another variable name than the last,
# * Python will assign values to the variable until the number of values left matches the number of variables left.

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green,*topic,red) = fruits
# print(green,topic,red) # * apple ['mango', 'papaya', 'pineapple'] cherry

# ? ################### Loop tuples ##################

# * basic loop through tuples

# for x in thisTuple:
#     print(x)

# * Loop Through the Index Numbers

# * You can also loop through the tuple items by referring to their index number.
# * Use the range() and len() functions to create a suitable iterable

# for i in range(len(thisTuple)):
#     print(thisTuple[i],i)

# * Using while loop 

# i = 0
# while i < len(thisTuple):
#     print(thisTuple[i])
#     i = i + 1


# ? ###################### Join Tuples ###############

# * To join two or more tuples we can use "+" operator

# tuple1 = ('apple','mango','orange')
# tuple2 = (1,2,3)
# tuple3 = tuple1 + tuple2

# print(tuple3)

# * Multiply tuples : If you want to multiply the content of a tuple a given number of times, you can use the * operator

# myTuple = thisTuple * 2
# print(myTuple) # * return ('apple', 'banana', 'orange', 'apple', 'banana', 'orange')

# ? ######### Tuple Methods ##########

# * index() : return index of passed argument in tuple
# print(thisTuple.index('orange'))
# if the value does not exist
# print(thisTuple.index('kiwi')) # ! ValueError: tuple.index(x): x not in tuple

# * count() : return no of count value present

# marksTuple = (24,51,35,24,56)
# print(marksTuple.count(35))

# * if passed value does not exist return 0
