"""
* PYTHON DICTIONARIES:
* Dictionaries are used to store data values in key:value pairs.
* A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# dict() : constructor to make dictionary

# newDict = dict(name = 'john',age = 26)
# print(newDict)

# * Accessing items

# x = thisDict['model']
# print(x)

# * Get Keys
# x = thisDict.keys()
# print(x)

# * Get Values

# x = thisDict.values()
# print(x)

# thisDict['year'] = 2024
# x = thisDict.values()
# print(x)

# * Get items() : method return each item in a dictionary, as tuples in list

# x = thisDict.items()
# print(x) # return : dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# * Check if the key exists

# if('model' in thisDict):
    # print('Yes, model key is in thisDict')

# print('model' in thisDict)

# * Change items

# * Update dictionary : The update() method will update the dictionary with the items from the given argument

# thisDict.update({'year':2024})
# thisDict.update({'type':'sport'})
# print(thisDict)

# * Adding items

# thisDict['color'] = 'red'
# print(thisDict)

# * Removing items

# * pop() : The pop() method removes the item with the specified key name:

# thisDict.pop('model')
# print(thisDict)

# * popitem() : method removes the last inserted item (in versions before 3.7, a random item is removed instead):

# thisDict.popitem()
# print(thisDict)

# * del : keyword removes the item with specified key name

# del thisDict["brand"]
# print(thisDict)

# * del : keyword also delete the dictionary completely
# del thisDict
# print(thisDict) # ! throw error : NameError: name 'thisDict' is not defined

# * clear() : method empties the dictionary

# thisDict.clear()
# print(thisDict) # return empty dictionary {}

# * Loop dictionaries

# * print all key names in dictionary
# for x in thisDict:
#     print(x)

# for x in thisDict.keys():
#     print(x)

# * print all values in dictionary

# for x in thisDict:
#     print(thisDict[x])

# for x in thisDict.values():
#     print(x)

# * Loop through both keys and values by items() method:

# for x,y in thisDict.items():
    # print('Key:'+ x , 'Value:' , y)

# * Copy dictionary

"""
    You cannot copy a dictionary simply by typing dict2 = dict1, 
    because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2
"""

# x = thisDict.copy()
# print(thisDict)
# x['color'] = 'red' # to see a difference 
# print(x)

# * another way to copy dictionary is using built-in function dict():

# x = dict(thisDict)
# print(x)

# * Nested dictionary

myFamily = {
      "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# * Access items in nested dictionary

# print(myFamily["child2"]['name'])

# * Loop through nested dictionary

# for x in myFamily.values():
#     for x,y in x.items():
#         print(x,y)