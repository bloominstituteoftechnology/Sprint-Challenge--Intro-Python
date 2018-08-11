import math

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
for x in humans:
    if x.name.startswith("D"):
        r.append(x)
# for i in humans:
#         r.append(i)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = []  # TODO
for x in humans:
    if x.name.endswith("e"):
        r.append(x)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
r = []  

# def filteredHumans(alphabet):
#     for x in humans:
#         for y in alphabet:
#             if x.name.startswith(y):
#                 r.append(x)


# for x in humans:
#     if x.name.startswith()

print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = []  

for i in humans:
    i.age = i.age + 10
    r.append(i)
    # print(i.age)

print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = [] 

for i in humans:
    string = i.name + "-" + str(i.age)
    r.append(string)

print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = []  

for i in humans:
    if i.age > 27 and i.age < 32:
        r.append(i)

print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
r = []  

for i in humans:
    i.name = i.name.upper()
    i.age = i.age + 5
    r.append(i)
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = [] 

for i in humans:
    sqroot = math.sqrt(i.age)
    r.append(sqroot)
print(r)