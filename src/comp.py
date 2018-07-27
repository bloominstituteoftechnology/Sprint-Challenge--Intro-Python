class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)


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
r = []
for person in humans:
    if person.name[0] == 'D':
        r.append(person.name)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = []
for person in humans:
    if person.name[len(person.name) - 1] == 'e':
        r.append(person.name)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

import re

print("Starts between C and G, inclusive:")
r = []
for person in humans:
    pattern = re.compile("[C-G]")
    if pattern.search(person.name[0]):
        r.append(person.name)
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = []
for person in humans:
    r.append(person.age + 10)
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = []
for person in humans:
    r.append("%s-%s" % (person.name, person.age))
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = []
for person in humans:
    if person.age <= 32 and person.age >= 27:
        r.append((person.name, person.age))
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
r = []
for person in humans:
    r.append((person.name.upper(), person.age + 5))
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []
import math
for person in humans:
    r.append(math.sqrt(person.age))
print(r)
