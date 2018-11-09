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
#  h=human
# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

# Human("David", 31), Human("Daphne", 30),

print("Starts with D:")
r = [h.name for h in humans if h.name[0]==('D')]  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

# Human("Alice", 29), Human("Charlie", 37),Human("Daphne", 30),Human("Eve", 26),

print("Ends with e:")
r = [h.name for h in humans if h.name[-1]==('e')]  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
#     cdefg
#     Human("Charlie", 37),
#     Human("Daphne", 30),
#     Human("Eve", 26),
#     Human("Frank", 18),
#     Human("Glenn", 42),
#     Human("David", 31),

print("Starts between C and G, inclusive:")
r = [h.name for h in humans if (h.name[0] >= 'C' and (h.name[0] <= 'G'))]  # TODO
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = [h.age + 10 for h in humans]  # TODO
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = [h.name + "-" + str(h.age) for h in humans]  # TODO
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = [(h.name, h.age) for h in humans if (h.age > 26) and (h.age < 33)]  # TODO
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The `humans` list should be unmodified.

# Human("Alice", 29) -->> Human("ALICE", 34)
print("All names capitalized:")
r = [Human(h.name.upper(), h.age + 5) for h in humans]  # TODO
# r = [(h.name.upper(), h.age + 5) for h in humans]
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = [math.sqrt(h.age) for h in humans]  # TODO
# r = [2**h.age for h in humans]
print(r)