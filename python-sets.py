""" 
    * PYTHON SETS 
    * Sets are used to store multiple items in a single variable.
    * Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
    * A set is a collection which is unordered, unchangeable*, and unindexed
"""

# ? ########## Sets basics ############

# * sets are write by curly brackets

fruitSet = {'apple','banana','cherry'}
# print(fruitSet) # * Sets are unordered, so you cannot be sure in which order the items will appear.

# * Set Items : unordered, unchangeable, and do not allow duplicate values.

# * Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

# carsSet = {'bmw','mercedes',True,1,2}
# print(carsSet)

# * Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
# carsSet = {'bmw','mercedes',False, 0,2}
# print(carsSet)

# * Get the length of set

# print(len(fruitSet))

# * Type()

# print(type(fruitSet)) # * <class set>

# * The set constructor

# markSet = set(('apple',53,True,82,42,65)) # note the double round-brackets
# print(markSet)

# ? ########## Access set items ##########

# * You cannot access items in a set by referring to an index or a key.
# * But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# for x in fruitSet:
#     print(x)

# print('banana' in fruitSet)
# print('banana' not in fruitSet)

# ? ############## Adding new item in set ##########

# * add(): method to add new item in set

# fruitSet.add('orange')

# print(fruitSet)

# * update() : adding items from another set

# set1 = {'apple','banana','orange'}
# set2 = {'kiwi','watermelon'}
# set1.update(set2)
# print(set1)

