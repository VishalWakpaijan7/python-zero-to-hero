"""
PYTHON REGEX :
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
"""

# * RegEx module: 

import re

txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#     print('Yes')
# else:
#     print('No')

# * The findall() function: the findall function returns a list containing all matches.

# x = re.findall('in',txt)
# print(x)
#? If no matches are found, an empty list is returned:

# * The search() function: 
"""
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:
"""

# x = re.search('\s',txt)
# print(x.start())

# x = re.search('Spain',txt)
# print(x.start())

# * The split() function: The split() function returns a list where the string has been split at each match:

# x = re.split('\s',txt)
# print(x)

# * The sub() function : replaces the matches with the text of your choice:

# x = re.sub("\s",'9',txt)
# print(x)

# * You can control the number of replacements by specifying the count parameter:

# x = re.sub("\s","9",txt,2)
# print(x)

