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
namesWithD = [Human.name for Human in humans if "D" in Human.name]  # TODO
print(namesWithD)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
namesWithe = [Human.name for Human in humans if "e" in Human.name[-1]]  # TODO
print(namesWithe)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
between = [Human.name for Human in humans if ord(Human.name[0]) in range(ord('C'), ord('G')+1)]
print(between)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
agesAdd = [Human.age + 10 for Human in humans]
print(agesAdd)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
newString = [Human.name + '-' + str(Human.age) for Human in humans]
print(newString)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
ageRange = [(Human.name, Human.age) for Human in humans if Human.age in range(27, 32)]
print(ageRange)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
newHumans = [[Human.name.upper(), Human.age + 5] for Human in humans]
print(newHumans)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
root = [math.sqrt(Human.age) for Human in humans]
print(root)




