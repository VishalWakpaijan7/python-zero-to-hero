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

# ? ################## Change in list items ############

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

# ? ################## Add list items ############

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

# ? ################## Remove list items ############

# * Remove method 
# fruitList.remove('apple')
# print(fruitList)

# * If there are more than one item with the specified value, the remove() method removes the first occurrence

# newFruits = ['apple', 'banana', 'orange', 'banana', 'pear']
# newFruits.remove('banana')
# print(newFruits)

# * Removed at specified index : The pop() method help us to remove list item at specified index

# fruitList.pop(2)  # Cherry removed at index 2
# print(fruitList)

# * If you do not specify the index, the pop() method removes the last item
# fruitList.pop() # mango removed
# print(fruitList) 

# * del keyword also removes the specified index

# del fruitList[2]
# print(fruitList)

# * del keyword also remove list completely
# del fruitList
# print(fruitList) # ! return NameError: name 'fruitList' is not defined

# * Clear the list : the clear() method empties the list, The list still remains, but it has no content

# fruitList.clear()
# print(fruitList) # * return []


# ? ################## Loop List ############

# * Loop through a list : we can loop through the list by using for loop

# for x in fruitList:
#     print(x)

# * Loop through index numbers : we can loop through list items by referring to their index number | use range() and len() function to create suitable iterable
# print(range(len(fruitList))) # ? return range from (0,7) 

# for i in range(len(fruitList)):
#     print(fruitList[i])

# * While loop : use len() function to determine the length of the list, then start at 0 and loop your way through the list 
# * by referring to their indexes

# i = 0
# while i < len(fruitList):
#     print(fruitList[i])
#     i = i + 1

# * Looping Using List Comprehension : list comprehension offer shortest syntax for looping through list

# [print(x) for x in fruitList]


# ? ################## List Comprehension ############
# * List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# * requirement : give new list of fruit names letter containing 'a'

# * With for loop
# newList = []
# for x in fruitList:
#     if( 'a' in x ):
#         newList.append(x)
# print(newList)
# * With list comprehension

# newList = [x for x in fruitList if 'a' in x]
# print(newList)

# newList = [x for x in fruitList if x != 'apple'] # * list comprehension will work with not condition as well and return new list with existing list values.
# print(newList)

# * In list comprehension iterable can be any iterable like: list,tuple set, range etc

# newList = [x for x in range(10)]
# print(newList)

# * same example with condition

# newList = [x for x in range(10) if x <= 5]
# print(newList)

# * Expression : The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list

# newList = [x.upper() for x in fruitList]
# print(newList)

# * You can set outcome to whatever you like

# newList = ['Hello' for x in range(5)]
# print(newList)

# * The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# newList = [x if x != 'banana' else 'orange' for x in fruitList]
# print(newList)

# ? ################## Sort List ############

# * List objects have a sort() method that will sort the list alphanumerically, ascending, by default

# fruitList.sort()
# print(fruitList)

# * Sort the list numerically

marksList = [ 23, 45, 75, 65, 10, 56 ]
# marksList.sort()
# print(marksList)

# * Sort descending : To sort descending, use the keyword argument reverse = True:
# fruitList.sort(reverse=True)
# print(fruitList)

# marksList.sort(reverse=True)
# print(marksList)

# * Customize sort function : You can also customize your own function by using the keyword argument key = function.
# * The function will return a number that will be used to sort the list (the lowest number first)

# def mySortFunc(n):
#     return abs(n - 50)

# marksList.sort(key=mySortFunc)

# print(marksList)

# * Case insensitive sort : 
# * By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

# membersList = ['vishal', 'sachin', 'Nitin', 'pratik', 'sunil', 'amol']
# membersList.sort()
# print(membersList)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function

# membersList.sort(key= str.lower) # * Use str.lower when need of case-insensitive sort function
# print(membersList)

# * Reverse order :
"""
* What if you want to reverse the order of a list, regardless of the alphabet?
* The reverse() method reverses the current sorting order of the elements
"""

# fruitList.reverse()
# print(fruitList)

# marksList.reverse()
# print(marksList)

