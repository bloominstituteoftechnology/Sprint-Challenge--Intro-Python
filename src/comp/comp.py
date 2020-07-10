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
# for d in humans:
#     if d.name[0] == 'D':
#         print(d.name)
a = [d.name for d in humans if d.name[0] == "D"]
# a = [d.name for d in humans if d.name.startswith('D')]
print(a)


# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
# for e in humans:
#     if e.name.endswith('e'):
#         print(e.name)
b = [e.name for e in humans if e.name[-1] == 'e']
# b = [e.name for e in humans if e.name.endswith('e')]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
# for cng in humans:
#     if cng.name[0] in ["C", "D", "E", "F", "G"]:
#         print(cng.name)
c = [cng.name for cng in humans if cng.name[0] in ["C", "D", "E", "F", "G"]]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
# for plus in humans:
#     print(plus.age + 10)
d = [plus.age + 10 for plus in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{layout.name}-{layout.age}" for layout in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(tup.name, tup.age)
     for tup in humans if tup.age in [27, 28, 29, 30, 31, 32]]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(up.name.upper(), up.age + 5) for up in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(sq.age) for sq in humans]
print(h)
