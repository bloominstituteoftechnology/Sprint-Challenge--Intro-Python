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

# Short Version *****
# a = [human.name for human in humans if human.name.startswith("D")]
# ****************************************

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

# For loop version
a = []
for human in humans:
    if human.name.startswith("D"):
        a.append(human.name)
print(f"Starts with D: {a}")

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

b = []
for human in humans:
    if human.name.endswith("e"):
        b.append(human.name)
print(f"Ends with e: {b}")

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

c = []
for human in humans:
    if any(human.name.startswith(x) for x in "CDEFG"):
        c.append(human.name)
print(f"Starts between C and G, inclusive: {c}")

# Write a list comprehension that creates a list of all the ages plus 10.

d = []
for human in humans:
    d.append(human.age + 10)
print(f"Ages plus 10: {d}")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.

e = []
for human in humans:
    e.append(human.name + "-" + str(human.age))
print(f"Name hyphen age: {e}")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

f = []
for human in humans:
    x = (human.name, human.age)
    if human.age in range(27, 33):
        f.append(x)
print(f'Names and ages between 27 and 32: {f}')

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
g = []
for human in humans:
    g.append(f"{human.name.upper()} - {human.age + 5}")
print(f"All names uppercase: {g}")

# Write a list comprehension that contains the square root of all the ages.
import math
h = []
for human in humans:
    h.append(math.sqrt(human.age))
print(f"Square root of ages: {h}")
