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
a = [str(humanoid.name) for humanoid in humans if humanoid.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [str(humanoid.name) for humanoid in humans if list(humanoid.name)[-1] == "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
letters = ['C', 'D', 'E', 'F', 'G']
c = [str(humanoid.name) for humanoid in humans if humanoid.name[0] in letters]
print(sorted(c))

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [int(humanoid.age + 10) for humanoid in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [str(f'{humanoid.name}-{humanoid.age}') for humanoid in humans]
print(sorted(e))

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(humanoid.name, humanoid.age) for humanoid in humans if humanoid.age >= 27 and humanoid.age <=32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase, 5 added to age:")
g = [Human((humanoid.name).upper(), (humanoid.age + 5)) for humanoid in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(humanoid.age) for humanoid in humans]
print(h)
