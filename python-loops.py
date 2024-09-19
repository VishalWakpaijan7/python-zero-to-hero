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