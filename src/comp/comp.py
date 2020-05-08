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

# created a list of names
names = []
for i in range(len(humans)):
  names.append(humans[i].name)

# created a list of ages
ages = []
for i in range(len(humans)):
  ages.append(humans[i].age)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
check = 'D'
a = [idx for idx in names if idx[0] == check]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
check = 'e'
b = [idx for idx in names if idx[-1] == check]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
check = ['C', 'D', 'E', 'F', 'G']
c = [idx for idx in names if idx[0] in check]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [age + 10 for age in ages]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for i in range(len(humans)):
  e.append((humans[i].name+'-'+str(humans[i].age)))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for i in range(len(humans)):
  if humans[i].age in range(27,33):
    f.append((humans[i].name, humans[i].age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for i in range(len(humans)):
  g.append((humans[i].name.upper(), humans[i].age + 5))
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for i in range(len(humans)):
  h.append(humans[i].age**.5)
print(h)
