#Python Data Types

#standard or built-in data types in Python

# Numeric Types
# Python supports three numeric types: int, float, and complex.
#
# int → Whole numbers
#
# float → Decimal numbers
#
# complex → Numbers with a real and imaginary part

x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Sequence Types
# Sequences store collections of items in a specific order.
#
# string → Immutable text
#
# list → Mutable ordered collection
#
# tuple → Immutable ordered collection

# 📚 Sequence Types
# Sequences store collections of items in a specific order.
#
# string → Immutable text
#
# list → Mutable ordered collection
#
# tuple → Immutable ordered collection

s = "Hello"             # string
lst = [1, 2, 3]         # list
tup = (4, 5, 6)         # tuple

print(s[0])   # 'H'
lst.append(4) # [1, 2, 3, 4]

# Mapping Type
# The most common mapping type is dict, which stores key-value pairs.

student = {"name": "Alice", "age": 21}
print(student["name"])   # Alice

# Boolean Type
# Booleans represent truth values: True or False.

is_active = True
print(is_active)        # True
print(5 > 3)            # True

# Set Types
# Sets store unique elements.
#
# set → Mutable
#
# frozenset → Immutable

nums = {1, 2, 3, 3}        # set → {1, 2, 3}
fnums = frozenset([1, 2, 2, 3])  # frozenset → {1, 2, 3}

# Binary Types
# Binary data types handle raw data.
#
# bytes → Immutable sequence of bytes
#
# bytearray → Mutable sequence of bytes
#
# memoryview → View of another binary object

b = bytes([65, 66, 67])       # b'ABC'
ba = bytearray([65, 66, 67])  # bytearray(b'ABC')
mv = memoryview(b)

print(b)   # b'ABC'
print(ba)  # bytearray(b'ABC')
print(mv[0])  # 65

# Python’s built-in data types are the foundation of programming in Python.
#
# Use numeric types for calculations.
#
# Use sequences for ordered data.
#
# Use dicts for key-value mappings.
#
# Use sets for unique collections.
#
# Use binary types for raw data handling.
