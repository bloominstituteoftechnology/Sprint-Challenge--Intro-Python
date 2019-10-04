# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

    def __str__(self):
        return self.__repr__(); #why whouldnt you do both of these?
    #repr replaces __str__ if not present, but it is good to have both 

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
for h in humans:
    if(len(h.name) < 1):
        continue;
    if(h.name[0] == "D"):
        a.append(h);
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for h in humans:
    if(len(h.name) < 1):
        continue;
    if(h.name[len(h.name)-1] == "e"):
        b.append(h);
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for h in humans:
    if(len(h.name) < 1):
        continue;
    if(h.name[0] >= "C" and h.name[0] <= "G"):
        c.append(h);
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for h in humans:
    d.append(h.age+10);
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for h in humans:
    e.append(h.name + "-" + str(h.age));
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for h in humans:
    if(h.age >= 27 and h.age <= 32):
        f.append((h.name,h.age));
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for h in humans:
    g.append(Human(h.name.upper(), h.age+5));
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
i = []
for h in humans:
    i.append(math.sqrt(h.age));
print(i)
