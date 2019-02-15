import re
# The following list comprehension exercises will make use of the 
# defined Human class. 
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
a = []
for x in humans:
    if x.name.startswith('D'):
        a.append(x.name)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for x in humans:
    if x.name.endswith('e'):
        b.append(x.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for x in humans:
    if re.match(r'[C-G]', x.name):
        c.append(x.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for x in humans:
    d.append(x.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for x in humans:
    e.append(x.name + '-' + str(x.age))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for x in humans: 
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
g = []
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
print(h)