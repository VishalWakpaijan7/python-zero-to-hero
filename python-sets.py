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

# * update() : adding items from another set or iterable

# set1 = {'apple','banana','orange'}
# list1 = list(('mango','pineapple'))
# set1.update(list1)
# set2 = {'kiwi','watermelon'}
# set1.update(set2)
# print(set1)

# ? ############## Remove Set Items ##########

# * To remove item in set use, remove() or discard method

# fruitSet.remove('apple')
# print(fruitSet)

# fruitSet.remove('kiwi') # ! throw error if the item to remove does not exist.
# print(fruitSet)

# fruitSet.discard('apple')
# print(fruitSet)

# fruitSet.discard('kiwi') # ? discard method does not throw error even if item to remove does not exist
# print(fruitSet)

"""
* You can also use the pop() method to remove an item,
* but this method will remove a random item, so you cannot be sure what item that gets removed
"""

# print(fruitSet.pop()) # *  return value of the pop() method is the removed item
# print(fruitSet)

# * Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# * Clear() : empties the set

# fruitSet.clear()
# print(fruitSet) #return  set()

# del fruitSet
# print(fruitSet) # * NameError: name 'fruitSet' is not defined

# ? Looping set

# for x in fruitSet:
#     print(x)

# ? Join sets
"""

* There are several methods to join two or more sets in python
* The union() and update() method joins all items from sets
* The intersection() method keeps ONLY duplicates
* The difference() method keeps the items from the first set that are not in the other set's 
* The symmetric_difference() method keeps all items EXCEPT the duplicate 
""" 

# * Union() : method return new set from all the items from both sets

# set1 = {'item1','item2','item3'}
# set2 = {'item5','item5','item6'}
# set3 = set1.union(set2)
# print(set3)

# set3 = set1 | set2 # * we can use | symbol as well
# print(set3)
 
# * Note: The "|" operator only allows you to join sets with sets,
# * and not with other data types like you can with the  union() method.

# * Update() : method insert all items from one set into another | and changes the original set, and does not return a new set.

# set1.update(set2)
# print(set1)

# * Both union() and update() will exclude any duplicate items.

# * Intersection() : method will return new set, that only contains the items that are present in both sets

# set1.add('item5')
# set3 = set1.intersection(set2)
# print(set3)

# * You can use the & operator instead of the intersection() method, and you will get the same result.

# set1.add('item5')
# set1.add('item6')
# set3 = set1 & set2
# print(set3)

# * Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# * intersection_update() : method will also keep duplicates, but it will change original set instead of returning a new set

# set1.add('item5')
# set1.intersection_update(set2)
# print(set1)
# * The values True and 1 are considered the same value. The same goes for False and 0
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set1.intersection_update(set2)
# print(set1)

# * Difference() : method return new set that will only contain items from first set that are not present in the other set.

set1 = {'apple','orange','cherry'}
set2 = {'google','microsoft','apple'}
# set3 = set1.difference(set2)
# print(set3)

# * You can use the - operator instead of the difference() method

# set3 = set1 - set2
# print(set3)

# * The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method

# * difference_update() : method will also keep the items from the first set that are not present in the other set, but it will change the original set instead of returning new set

# set1.difference_update(set2)
# print(set1)

# * symmetric_difference() : method will keep only the elements that are NOT present in both sets

# set3 = set1.symmetric_difference(set2)
# print(set3)

# * can use ^ operator instead symmetric_difference() method,

# set3 = set1 ^ set2
# print(set3)

# * The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set

# set1.symmetric_difference_update(set2)
# print(set1)