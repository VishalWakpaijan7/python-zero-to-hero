""" 
 * PYTHON LISTS

 * List is use to store multiple data in a single variable.
 * Lists are one of the 4 built-in data types in python used to store collection of data, the other 3 are tuple, set, dictionary
 * all with different qualities and usage
"""

fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruitList)

# * List items : 
# ? List items are ordered, changeable, and allow duplicate values | items are indexed

# * What ordered means ? :
# ? It means that the items have defined order, and that order will not change.
# ? If you add new items to a list, the new items will be placed at end of the list.

# ? Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# * List it changeable it meaning it can be change, add, and remove items in list after it's created

# * Allow duplicate : Since the lists are indexed list can items with the same value

# * List length: To determine how many items a list has, use the len() function
# print(len(fruitList))

# * What it type of list ?
#  ? From Python's perspective, lists are defined as objects with the data type 'list':
# print(type(fruitList)) # <class 'list'>

# * The list() constructor : It is also possible to use the list() constructor when creating a new list

# carsList = list(('tata', 'suzuki', 'fiat')) # ? note the double round-brackets
# print(type(carsList),carsList)

"""
 * Python Collections (Arrays)
    ? There are four collection data types in the Python programming language:
    ? List is a collection which is ordered and changeable. Allows duplicate members.
    ? Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    ? Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. (*Set items are unchangeable, but you can remove and/or add items whenever you like.)
    ? Dictionary is a collection which is ordered** and changeable. No duplicate members.( As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. )
"""

# * Access Items : List items are indexed and you can access them by referring to the index numbers:
# print(fruitList[1])

# * Negative indexing:
# print(fruitList[-2]) # Negative indexing means start from the end

# * Range of indexes
# print(fruitList[2:5]) # ? The search will start at index 2 (included) and end at index 5 (not included).

# print(fruitList[:5]) # ? leaving out the start value, the range will start at the first item 
# # ? ( leaving out the start value, the range will start at the first item ) 

# print(fruitList[2:]) # ? leaving out the end value, the range will go on to the end of the list
# # ? (  returns the items from "cherry" to the end ) 

# * Range of negative index 
# ? Specify negative indexes if you want to start the search from the end of the list
# print(fruitList[-5:-2]) not include "melon"

# * Check if item exist

# print('apple' in fruitList)
# print('dragon-fruit' in fruitList)

# if 'apple' in fruitList:
#     print("Yes, 'apple' is in the fruits list")

# * ################## Change in list items ############

# * Change item value : To change the value of a specific item, refer to the index number

# fruitList[1] = "dragon-fruit"
# print(fruitList)

# * Change a Range of Item Values
# ? To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values

# fruitList[1:3] = ['dragon-fruit','pear','watermelon']
# print(fruitList, len(fruitList))

# * If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
# * Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# * Insert Items 
"""
 * To insert a new list item, without replacing any of the existing values, we can use the insert() method.
 * The insert() method inserts an item at the specified index
"""
# fruitList.insert(2,'watermelon')
# print(fruitList)

# * ################## Add list items ############

# * Append items : to add an item to the end of the list use append() method

# fruitList.append('pear')
# print(fruitList)

# * Insert items : To insert a list item at a specified index, use the insert() method. : The insert() method inserts an item at the specified index

# fruitList.insert(1,'pear')
# print(fruitList)

# * Extend list : To append elements for another list to the current list use extend() method.

# tropical = ["pineapple", "papaya"]
# fruitList.extend(tropical) # * The elements will be added to the end of the list
# print(fruitList)

# * The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

# tropicalTuple = ('pineapple','papaya')

# fruitList.extend(tropicalTuple)

# print(fruitList)

