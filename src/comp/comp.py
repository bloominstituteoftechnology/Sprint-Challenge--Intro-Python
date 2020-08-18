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
# print("Starts with D:")

a = [(i.name) for i in humans if i.name.startswith("D") == True ]

# for i in humans:
#     test = i.name.startswith("D")
    
#     if test == True:
#         a.append((i.name, i.age))
#     print(test)

# print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
# print("Ends with e:")
b = [(i.name) for i in humans if i.name.endswith("e") == True]

# for i in humans:
#     test = i.name.endswith("e")

#     if test == True:
#         b.append((i.name))
#     print(test)


# print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
# print("Starts between C and G, inclusive:")
c = [(i.name) for i in humans if i.name.startswith(("C", "D", "E", "F", "G")) == True ]

# for i in humans:
#     test = i.name.startswith(("C", "D", "E", "F", "G"))

#     if test == True:
#         print((i.name))
# print(i)

# print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
# print("Ages plus 10:")
d = [i.age + 10 for i in humans]

# for i in humans:
#     d.append(i.age + 10)
#     print(i.age + 10)
# *** reference the object attributes using "i.attribute" syntax ***

# print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
# print("Name hyphen age:")
e = [f"{i.name }-{i.age}" for i in humans]

# for i in humans:
#     print(f"{i.name } - {i.age}")
# print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
# print("Names and ages between 27 and 32:")

f = [(i.name, i.age) for i in humans if i.age >= 27 and i.age <= 32]

# for i in humans:
#     if i.age >= 27 and i.age <= 32:
#         age_tuple = []
#         age_tuple.append((i.name, i.age))
#         print(list(age_tuple))
        

# print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
# print("All names uppercase:")
g = [(Human(i.name.upper(), i.age + 5)) for i in humans]

# for i in humans:
#     new_humans = []
#     new_humans.append(Human(i.name.upper(), i.age + 5))
#     print(new_humans)

print(g)

# Write a list comprehension that contains the square root of all the ages.
# print("Square root of ages:")
import math
h = [math.sqrt(i.age) for i in humans]

# for i in humans:
#     new_age = []
#     new_age.append(i.age ** 2)
#     print(new_age)

# print(h)
