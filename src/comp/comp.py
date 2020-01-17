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

# print(help(humans))

# print(humans[0])
# human1 = str(humans[0])
# human3 = str(humans[0])[8]
# human2 = human1[8]
# print(human3)
print(str(humans).split()[2][0:2])

# for human in humans:
#     print(str(human).split())
#
# for human in humans:
#     print(str(human).split()[1][-2])

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [str(human).split()[1][:-1] for human in humans if str(human).split()[1][0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [str(human).split()[1][:-1] for human in humans if str(human).split()[1][-2] == 'e']
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [str(human).split()[1][:-1] for human in humans if str(human).split()[1][0] in ['C','D','E','F','G']]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [10 + int(str(human).split()[2][0:2]) for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [str(human).split()[1][:-1] + '-' + (str(human).split()[2][0:2]) for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(str(human).split()[1][:-1], int(str(human).split()[2][0:2])) for human in humans if int(str(human).split()[2][0:2]) in range(27, 33)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [(Human((str(human).split()[1][:-1]).upper(), (int(str(human).split()[2][0:2]) + 5))) for human in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(int(str(human).split()[2][0:2])) for human in humans]
print(h)
