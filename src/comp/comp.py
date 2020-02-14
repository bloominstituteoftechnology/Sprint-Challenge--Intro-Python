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

# (1) Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("\n")
print("(1) Starts with D:")
a = []
for human in humans:
    if human.name[0] == "D":
        a.append(human)

print(a)
print("\n")
# (2) Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("(2) Ends with e:")
b = []
for human in humans:
    if human.name[-1] == "e":
        b.append(human)

print(b)
print("\n")

# (3) Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("(3) Starts between C and G, inclusive:")
c = []
for human in humans:
    first_letter = ord(human.name[0])
    if first_letter in range(ord('C'), ord('G')+1):
        c.append(human)
print(c)
print("\n")

# (4) Write a list comprehension that creates a list of all the ages plus 10.
print("(4) Ages plus 10:")
d = []
for human in humans:
    time_warp_human = Human(human.name, human.age + 10)
    d.append(time_warp_human)
print(d)
print("\n")

# (5) Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("(5) Name hyphen age:")
e = []
for human in humans:
    new_str = f"{human.name}-{human.age}"
    e.append(new_str)
print(e)
print("\n")

# (6) Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("(6) Names and ages between 27 and 32:")
f = []
for human in humans:
    if human.age in range(27, 32+1):
        human_tup = (human.name, human.age)
        f.append(human_tup)
print(f)
print("\n")

# (7) Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("(7) All names uppercase:")
g = []
print(g)

# (8) Write a list comprehension that contains the square root of all the ages.
print("(8) Square root of ages:")
import math
h = []
print(h)
