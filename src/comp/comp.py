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
a = [d_names.name for d_names in humans if str(d_names.name[0]) == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [ends_e.name for ends_e in humans
     if str(ends_e.name[int(len(ends_e.name) -1)]) == "e"]
print(b)
# for i in humans:
#     if i.name[-1] == 'e':
#         b.append(i.name)


# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)
c = [person.name for person in humans if person.name[0] in char_range("C", "G")]
print(c)

# for i in humans:
#     if i.name[0].upper() >= 'C' and i.name[0].upper() <= 'G':
#         c.append(i.name)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [age.age + 10 for age in humans]
print(d)

# for i in humans:
#     d.append(i.age + 10)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{person.name}-{person.age}" for person in humans]
print(e)

# for i in humans:
#     e.append(f"{i.name}-{i.age}")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(person.name, person.age) for person in humans if person.age in range(27, 33, 1)]
print(f)
# for i in humans:
#     if i.age >= 27 and i.age <= 32:
#         human_tuple = (i.name, i.age)
#         f.append(human_tuple)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [(Human(people.name.upper(), people.age + 5)) for people in humans]
print(g)
# for i in humans:
#     new_human = (Human(i.name.upper(), i.age + 5))
#     g.append(new_human)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(person.age) for person in humans]
print(h)
# for i in humans:
    # root = math.sqrt(i.age)
    # h.append(root)
