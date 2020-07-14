# tuples.py
# showing tuples


class animal:
    LegsNumber = 0
    
    def __init__(self, legs = 0):
        self.LegsNumber = legs

# the basic
t = 12345, 54321, "hello"
# it contains diferent types
print(t[0])
print (t)
# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
print(u)
# The are immutable
# t[0] = 88888
# you can add multiple objects
v = ([1,2,3], "hello")
print(v)

dog = animal()
dog.LegsNumber = 4;

print(dog.LegsNumber)

print("Tuble with Multiple object types")
animals = [1, 2, 3], 'A DOG', ('DOG LEGS', dog)
print(animals)

# Build empty tuple
empty = ()      # with empty closed parentesis
print(len(empty))

# Tuple with a single value
singleton = 'Just one value',      # defined by the coma at end of the line
print(len(singleton))

# It's possible to unpacking the elements of a tuple into variables
# Just assign with the same number of variables than elements
myTuple = (123, 456, 789)
print(myTuple)
x, y, z = myTuple
print(x)
print(y)
print(z)