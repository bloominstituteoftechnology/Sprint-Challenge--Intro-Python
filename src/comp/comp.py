# The following list comprehension exercises will make use of the
# defined Human class.
import math


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

# print((humans[3].name[0]))

# if humans[3].name[0]:
#     pass


# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
# print(type(a))
for h in humans:
    if h.name[0] == "D":
        # print((h.name))
        a.append(h.name)
        # a.insert(h.name)
        # a.extend(h.name)


print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for h in humans:
    if h.name[-1:] == 'e':
        b.append(h.name)



print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

# print('****', humans[3].name[0:1])


print("Starts between C and G, inclusive:")
c = []
for h in humans:
    if h.name[0:1] == 'C':
        c.append(h.name)
    elif h.name[0:1] == "D":
        c.append(h.name)
    elif h.name[0:1] == "E":
        c.append(h.name)
    elif h.name[0:1] == "F":
        c.append(h.name)
    elif h.name[0:1] == "G":
        c.append(h.name)


print(c)

# Write a list comprehension that creates a list of all the ages plus 10.

# print("*******", (humans[4].age))


print("Ages plus 10:")
d = []

for human in humans:
    d.append(human.age+10)
    # d.insert(4, 10)


print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.


# print('*****XXXX', (humans[6].name + "-" + str(humans[6].age)))

print("Name hyphen age:")
e = []


for human in humans:
    e.append(human.name + "-" + str(human.age))


print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for human in humans:
    if human.age >= 27 and human.age <= 32:
        pre_f = []
        pre_f.append(human.name + ',' + str(human.age))
        tuple(pre_f)
        f.append(pre_f)
        # f.append()


print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
old_humans_list = humans
print('THIS IS THE OLD HUMANS ', old_humans_list)
new_humans_list = []

new_humans_list = humans.copy()
print('THIS IS NEW ', new_humans_list[3].name.upper())
print('THIS IS NEW ', new_humans_list[3].age + 5)


print("All names uppercase:")
print(humans)
g = []

for human in humans:
    # new_humans = []
    g.append(human.name.upper())
    # print(g)
    g.append(human.age + 5)
    # print(g)


print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")

h = []

for human in humans:
    h.append(math.sqrt(human.age))


print(h)
