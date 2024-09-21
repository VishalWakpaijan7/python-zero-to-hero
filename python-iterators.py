"""
* Python Iterators:
* An iterator is an object what contains a countable number of values
* An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

* Technically, in Python, an iterator is an object which implements the iterator protocol,
* which consist of the methods __iter__() and __next__().
"""

# * Iterator vs Iterable: Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from

# my_tuple = ('apple','orange','banana')
# my_iterator = iter(my_tuple)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# * Event string are iterable objects and can return iterator 

# my_str = 'banana'
# my_iterator = iter(my_str)
# print(next(my_iterator))

# * Looping through an iterator

# myTuple = ('apple','banana','cherry')

# # for x in myTuple:
# #     print(x)

# myString = 'banana'

# for x in myString:
#     print(x)

# * Create an Iterator 

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
    
# my_number = MyNumber()
# my_iter = iter(my_number)

# print(next(my_iter))
# print(next(my_iter))

# * Stopiteration
"""
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
To prevent the iteration from going on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
"""

# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:raise StopIteration

# my_class = MyNumber()
# my_iter = iter(my_class)

# for x in my_iter:
#     print(x)

