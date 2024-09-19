"""
* Python has two primitive loop commands:
* 1.while: loop
* 2.for: loop
"""

# * The while loop: while loop we can execute a set of statements as long as a condition is true

# i = 1

# while i < 6:
#     print(i)
#     i += 1 # * Note: remember to increment i, or else the loop will continue forever.

# * The brake statement : the break statement we can stop the loop even if the while condition is true

# i = 1

# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# * The continue statement: the continue statement we can stop the current iteration, and continue with the next

# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         # print('Hey')
#         continue
#     print(i)

# * The else statement: else statement we can run a block of code once when the condition no longer is true:

# i = 1
# while i < 6:
#     print(i)
#     i +=1
# else: print('i is no longer less than 6')

"""
*For loop:
 * A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
 *This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
 *With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
"""

fruit = ['apple','banana','cherry']

# for x in fruit:
#     print(x)

# * Looping through a string

# for x in 'banana':
#     print(x)

# * The break statement

# for x in fruit:
#     print(x)
#     if x == 'banana':
#         break

# for x in fruit:
#     if x == 'banana': break
#     print(x)

# * The continue statement

# for x in fruit:
#     if x == 'banana':continue
#     print(x)

# * The else if for loop

# for x in range(6):
#     print(x)
# else:print('for loop finished')

# ? Note: The else block will NOT be executed if the loop is stopped by a break statement

# for x in range(6):
#     if x == 3:break
#     print(x)
# else:print('loop finished')

# * Nested loops : The "inner loop" will be executed one time for each iteration of the "outer loop"

# carsList = ['bmw','ford','fiat']
# for x in carsList:
#     for y in fruit:
#         print(x , y)

# * Pass statement 

# for x in [1,2,3]:
#     pass