# PYTHON STRINGS

# Quotes inside quotes

# print("It's alright")
# print("He is called 'johnny'")
# print('He is called "johnny"')

# assigning string to variable
# a = 'hello'

# multiline strings

# b = """ Hey, Vishal
# You are hero! believe in your self
# """
# print(b)

# Note: in the result, the line breaks are inserted at the same position as in the code.

# String are Arrays

# a = 'Hello, World!'
# print(a[0])

""" Looping through a string """  
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# x = 'Hello, World!'
# for x in x:
#     print(x)

""" String length """
# a = 'Vishal Wakpaijan'
# print(len(a))

""" Check string """
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# txt = "The best things in life are free"
# print('free' in txt) # True
# if 'free' in txt:
    # print("Yes, 'free' is present")

""" Check if not """
# print('expensive' not in txt) # True

# if 'expensive' not in txt:
#     print("No, 'expensive' is NOT present.")

""" Python - Slicing Strings """

""" 
Slicing: You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.

"""

# b = 'Hello, World!'
# print(b[2:8]) # Get the characters from position 2 to position 8 (not included):

""" Slice from the start """
# print(b[:5]) # Get the characters from the start to position 5 (not included):

""" Slice to the end """
# print(b[2:])

""" Negative Indexing
    "Get the characters: From: "o" in "World!" (position -5)
    To, but not included: "d" in "World!" (position -2)
"""
# print(b[-5:-2])

""" Modify Strings """

""" Upper Case """

# a = 'Hello, World!'
# print(a.upper()) # Convert to HELLO, WORLD!

""" Lower Case """
# print(a.lower()) # Convert to hello, world!

""" Remove Whitespace """
# b = " Hello, World!  "
# print(b.strip()) # Hello, World!

""" Replace String """
# print(a.replace('H','J')) # Jello, World!

""" Split String : The split() method returns a list where the text between the specified separator becomes the list items. """
# print(a.split(",")) #  returns ['Hello', ' World!']

""" #################### STRING CONCATENATION ####################### """
# To concat or combine two string we can use + operator

a = 'Hello'
b = 'World'

c = a + b
# print(c) # return HelloWorld

# to add space between them

# print(a + " " + b) # return Hello World

""" #################### FORMAT STRING ####################### """

# As we learn we cannot combine string with number like this
# print('Hello Vishal!' + 25) # Throws : TypeError: can only concatenate str (not "int") to str

""" But we can combine strings and numbers by using f-strings or the format() method! """

""" F-Strings: To specify a string as an f-string,
    simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
"""

# print(f"My name is John, I am {25} years old")

""" Placeholders and Modifiers """
# A placeholder can contain variables, operations, functions, and modifiers to format the value.

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

"""
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
"""

# txt = f"The price is {price:.8f} dollars"
# print(txt)

# A placeholder can contain Python code, like math operations:

# txt = f"The price is {20 * price} dollars"
# print(txt)

""" #################### ESCAPE CHARACTERS ####################### """

""" 
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash "\" followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

"""

# txt = "We are the so-called \"vikings\" from the north"
# print(txt)

# print('Single Quote:', 'Hey it\'s, me.')
# print('Back slash:', 'This will insert one \\ backslash')
# print('New line:', 'Hello \n World')
# print('Hello\n \rWorld!') #\r carriage returns
# print('Hello\tWorld!') # add one tab space between string
# print('HelloWorld\b!') # remove last character from where \b added simple words do backspace
# print('Hello\fWorld') # smilier to new line \n but add last to full back

#A backslash followed by three integers will result in a octal value:
# txt = "\110\145\154\154\157"
# print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 


""" ############# STRING METHODS #################### """
# Python has a set of built-in methods that you can use on strings.

""" Note: All string methods return new values. They do not change the original string. """
 
""" capitalize() : Converts the first character to upper case and rest to lowercase """
# print('python is FUN!'.capitalize())
# print('38 is my age.'.capitalize()) # nothings changes even if string number at start on string

""" casefold() : Converts string into lower case 
    This method is similar to the lower() method, but the casefold() method is stronger, more aggressive,
    meaning that it will convert more characters into lower case,
    and will find more matches when comparing two strings and both are converted using the casefold() method.
"""

# txt = 'Hello, And Welcome To My World!'
# print(txt.casefold())
# print(txt.lower()) can use lower as well

""" center() : The center() method will center align the string, using a specified character (space is default) as the fill character. """
# print('banana'.center(10))
# print('vishal'.center(20,'O')) # return : OOOOOOOvishalOOOOOOO

""" count(): The count() method returns the number of times a specified value appears in the string. """

# print('Vishal Wakpaijan'.count('a')) # return 4
# print('I love apples, apple are my favorite fruit'.count('apple',10,24))

""" encode(): The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used. """
# print('Hey vishal is here'.encode())

""" endswith(): The endswith() method returns True if the string ends with the specified value, otherwise False."""
# print('Hey, Vishal this is me god'.endswith('god')) True
# print('Hey, Vishal this is me god'.endswith('.')) False

""" expandtabs(): The expandtabs() method sets the tab size to the specified number of whitespaces. """

# print('H\te\tl\tl\to'.expandtabs(2))

# print('\t*'.expandtabs(3))
# print('\t*\t*'.expandtabs(2))
# print('\t*\t*\t*'.expandtabs(1))
# print('\t*\t*'.expandtabs(2))
# print('\t*'.expandtabs(3))

""" find(): Searches the string for a specified value and returns the position of where it was found """

# print('Hey, welcome to my world'.find('my',10)) # return index of "my" at 16

""" 
format(): The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
The format() method returns the formatted string.
"""

# txt = 'For only {price:.2f} dollars!'
# print(txt.format(price = 25)) # return For only 25.00 dollars!
# The Placeholders
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

# print('My name is {fname} and i am {age} years old!'.format(fname = 'vishal', age = 25))
# print('My name is {0} and i am {1} years old!'.format('John',36))
# print('My name is {} and i am {} years old!'.format('Jane',22))

""" Formatting Types """
# print('We have {:<100} chickens. formatting {}'.format(49,'left-align value'))
# print('We have {:>100} chickens. formatting {}'.format(49,'right-align value'))
# print('We have {:^100} chickens. formatting {}'.format(49,'center-align value'))
# print('We have {:=100} chickens. formatting {}'.format(-49,'sign-left most position'))
# print('The temperature is between {:+} and {:+} degrees celsius. formatting {}'.format(-5,7,'indicate if the number is positive or negative'))
# print('The temperature is between {:-} and {:-} degrees celsius. formatting {}'.format(-5,7,'indicate if the number is negative (positive numbers are displayed without any sign)'))
# print('The temperature is between {: } and {: } degrees celsius.'.format(-8,10,'Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers'))

""" index() : Searches the string for a specified value and returns the position of where it was found 
    The index() method is almost the same as the find() method,
    the only difference is that the find() method returns -1 if the value is not found.
"""

# print('Hey, I am superman'.index('am')) # return index of substring passed as argument

""" isalnum() : The isalnum() method returns True if all the characters are alphanumeric,
    meaning alphabet letter (a-z) and numbers (0-9).
    Example of characters that are not alphanumeric: (space)!#%&? etc.
"""

# print('company123'.isalnum()) # True
# print('company12 3#$#'.isalnum()) # False

""" isalpha() : The isalpha() method returns True if all the characters are alphabet letters (a-z).
    Example of characters that are not alphabet letters: (space)!#%&? etc. 
"""

# print('Hello'.isalpha())

""" isdecimal() : The isdecimal() method returns True if all the characters are decimals (0-9).
    This method can also be used on unicode objects. See example below.
"""

# print('1234.5'.isdecimal())

""" isdigit() : The isdigit() method returns True if all the characters are digits, otherwise False.
    Exponents, like ², are also considered to be a digit.
"""

# print('156456'.isdecimal()) # True
# print('156456a'.isdecimal()) # False