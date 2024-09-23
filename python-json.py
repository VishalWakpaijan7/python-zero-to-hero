"""
PYTHON JSON:
    JSON is a syntax for storing and exchanging data.
    JSON is text, written with JavaScript object notation.
"""

# * JSON Python: Python has a built-in package called json, which can be used to work with JSON data.

import json

# * Parse JSON - Convert from JSON to Python
# * If you have a JSON string, you can parse it by using the json.loads() method.

# * The result will be a Python dictionary.
# x = '{"name":"John","age": 30, "city":"New York"}'
# y = json.loads(x)
# print(y['age'])

# * Convert from python to json

# x = {
#     'name':'John',
#     'age':30,
#     'city':'new york',
# }
# y = json.dumps(x)
# print(y)
# print(type(y))

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# * Convert a Python object containing all the legal data types:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# print(json.dumps(x))

# * Format the Result : 
"""
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
The json.dumps() method has parameters to make it easier to read the result:
"""

# print(json.dumps(x, indent=4))

"""
You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
"""
# print(json.dumps(x,indent=4,separators=('.','=')))

# * Order the result: Use the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x,indent=4,sort_keys=True))