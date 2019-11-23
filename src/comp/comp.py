import string
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

for names in humans:
    if(names.name[0] == "D"):
        a.append(names.name)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []

for names in humans:
    nLength = len(names.name) - 1
    if(names.name[nLength] == "e"):
      b.append(names.name)  

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

alphaList = list(string.ascii_uppercase)

for names in humans:
    for letter in alphaList[2:7]:
        if(letter in names.name[0]):
            c.append(names.name)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []

for ages in humans:
    age = ages.age + 10
    d.append(age)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []

for human in humans:
   e.append(f'{human.name}-{human.age}')
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for person in humans:
    if (person.age >=27 and person.age <= 32):
        f.append((person.name, person.age))

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []

for person in humans:
    upperName = person.name.upper()
    agePlusFive = person.age + 5

    g.append(Human(upperName, agePlusFive) )

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []

for ages in humans:
    age = math.sqrt(ages.age)
    h.append(age)

print(h)
