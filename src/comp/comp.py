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
for human in humans:
    if human.name[0] == "D"
        a.append(human)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for human in humans:
    if human.name[-1] == "e"
        b.append(human)

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for human in humans:
    first_letter = ord(human.name[0])
    if first_letter in range(ord('C'), ord('G')+1):
        c.append(human)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for human in humans:
    age_human = Human(human.name, human.age + 10)
    d.append(age_human)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for human in humans:
    new_str = f"{human.name}-{human.age}"
    e.append(new_str)
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for human in humans:
    if human.age in range(27, 32+1):
        human_tup = (human.name, human.age)
        f.append(human_tup)
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for human in humans:
    cap_name = Human(human.name.upper(), human.age +5)
    g.append(cap_name)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for human in humans:
    srt_age = math.sqrt(human.age)
    h.append(srt_age)
print(h)
