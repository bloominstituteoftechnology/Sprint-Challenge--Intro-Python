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
r = [human.name for human in humans if human.name[0] == "D"]  # for in loop with in line if as a list comprehension using [] notation to select the first letter of each name
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = [human.name for human in humans if human.name[-1] == "e"]  # for in loop with in line if as a list comprehension using [] notation to select the last letter of each name
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = [human.name for human in humans if human.name[0] in ['C,', 'D', 'E', 'F', 'G']]  # for in loop with an in line if in conditional using a nested list with a list comprehension and [] notation to grab the first letter in each name 
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = [human.age + 10 for human in humans]  # for in loop adding 10 to each age using a list comprehension
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = [human.name + '-' + str(human.age) for human in humans]  # for in loop concatonating the name and age with a - between them using a list comprehension
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = [(human.name, human.age) for human in humans if human.age >= 27 and human.age <= 32]  # for in loop using an if conditional with the and operator to check that the age is between 27 and 32 using a list comprehension
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The `humans` list should be unmodified.
print("All names capitalized:")
r = []  # TODO
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []  # TODO
print(r)