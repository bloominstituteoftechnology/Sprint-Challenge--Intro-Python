# The following list comprehension exercises will make use of the
# defined Human class.

import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [item.name for item in humans if item.name.startswith('D')]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [item.name for item in humans if item.name.endswith('e')]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [item.name for item in humans if item.name.startswith(
    'C') or item.name.startswith('D') or item.name.startswith('E') or item.name.startswith('F') or item.name.startswith('G')]
print(c)
c = [name for name in humans if name.name[0] in "CDEFG"]
# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [item.age + 10 for item in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{item.name}-{item.age}" for item in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(item.name, item.age) for item in humans if item.age == 27 or item.age ==
     28 or item.age == 29 or item.age == 30 or item.age == 31 or item.age == 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(item.name.upper(), item.age + 5) for item in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(item.age) for item in humans]
print(h)
