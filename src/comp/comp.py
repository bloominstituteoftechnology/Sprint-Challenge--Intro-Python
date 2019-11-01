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
[ a.append(i.name) for i in humans if i.name.startswith("D") ]
# for i in humans:
#     if i.name.startswith("D"):
#         a.append(i.name)
print(a)


# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
[b.append(i.name) for i in humans if i.name.endswith("e")]

# for i in humans:
#   if i.name.endswith("e"):
#     b.append(i.name)


print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
# a = []
# for i in humans:
#     if i.name.startswith("D"):
#         a.append(i.name)
# print(a)

print("Starts between C and G, inclusive:")
my_range = "CDEFG"
c = []
for i in humans:
    if any(i.name.startswith(x) for x in my_range):
        c.append(i.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i.age +10 for i in humans]
# for i in humans:
#     age2 = i.age + 10
#     d.append(age2)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [i.name + '-' + str(i.age) for i in humans]
# for i in humans:
#   new_str = i.name + '-'+ str(i.age)
#   e.append(new_str)


print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f=[]
f= [(i.name, i.age) for i in humans if 27 < i.age <= 32]

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(i.name.upper(), i.age + 5) for i in humans]
# for i in humans:
#     new_human = Human(i.name.upper(), i.age + 5)
#     g.append(new_human)


# for i in humans:
#   uppercase = i.name.upper()
#   g.append(uppercase)

# for i in humans:
#   five = i.age +5
#   g.append(uppercase)

print(g)

# Write a list comprehension that contains the square root of all the ages.
import math
# h = []
h = [math.sqrt(i.age) for i in humans]
# for i in humans:
#     root = math.sqrt(i.age)
#     h.append(root)
print(h)