"""
* Python if-else:
 * Equals: a == b
 * Not Equals: a != b
 * Less than: a < b
 * Less than or equal to: a <= b
 * Greater than: a > b
 * Greater than or equal to: a >= b
* These conditions can be used in several ways, most commonly in "if statements" and loops.
* An "if statement" is written by using the if keyword
"""

a = 41
b = 4

# if a < b:
#     print('a is less then b')

# * ElIf : The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"

# if a > b:
#     print('Yes, a is greater than b')
# elif a == b:
#     print('a equals to b')
# else:print('a and b is not equal')

# * Short Hand If : you have only one statement to execute, you can put it on the same line as the if statement

# if a < b:print('a is less than b')

# * Short Hand If ... Else :  you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# print('A') if a > b else print("B") # * This technique is known as Ternary Operators, or Conditional Expressions.

# * multiple else statements on the same line

# print("A") if a > b else print("=") if a == b else print('B')

# * AND

c = 8

# if a > b and c > a:
#     print('Both condition are true')

# * OR

# if a > b or a > c:
#     print('At least one of the conditions are true')

# * NOT : not keyword is a logical operator, and is used to reverse the result of the conditional statement

# if not a > b:
#     print('a is not greater than b')

# * Nested if : You can have if statements inside if statements, this is called nested if statements

# if a > 10:
#     print('above then')
#     if a > 20:
#         print('and also above 20!')
#     else:
#         print('bot not above 20.')

# * The pass statement : if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error

# if b < a:
#     pass