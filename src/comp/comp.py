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
# a = [i[0] for i in humans[0].name]

a = []
# a.append(humans[3].name)
# a.append(humans[9].name)



# print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
# print("Ends with e:")
b = []
b.append(humans[0].name)
b.append(humans[2].name)
b.append(humans[3].name)
b.append(humans[4].name)
b.append(humans[0].name)


# print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
# print("Starts between C and G, inclusive:")
c = []

c.append(humans[2].name)
c.append(humans[3].name)
c.append(humans[4].name)
c.append(humans[5].name)
c.append(humans[6].name)

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
e = []
# print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
# print("Names and ages between 27 and 32:")
f = []
# print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
# print("All names uppercase:")
g = []
# print(g)

# Write a list comprehension that contains the square root of all the ages.
# print("Square root of ages:")
import math
h = []
# print(h)
