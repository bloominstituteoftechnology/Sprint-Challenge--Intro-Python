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
a = [h.name for h in humans if h.name[0] == "D"]
print(a)
# ['Daphne', 'David']
print("\n-----------------------------------------------\n")

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [h.name for h in humans if h.name[-1] == "e"]
print(b)
# ['Alice', 'Charlie', 'Daphne', 'Eve']
print("\n-----------------------------------------------\n")

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [h.name for h in humans if h.name[0] in ("C", "D", "E", "F", "G")]
print(c)
# ['Charlie', 'Daphne', 'Eve', 'Frank', 'Glenn', 'David']
print("\n-----------------------------------------------\n")

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [h.age + 10 for h in humans]
print(d)
# [39, 42, 47, 40, 36, 28, 52, 22, 51, 41]
print("\n-----------------------------------------------\n")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{h.name}-{h.age}" for h in humans]
print(e)
# ['Alice-29', 'Bob-32', 'Charlie-37', 'Daphne-30', 'Eve-26', 'Frank-18', 'Glenn-42', 'Harrison-12', 'Igon-41', 'David-31']
print("\n-----------------------------------------------\n")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(h.name, h.age) for h in humans if (h.age >=27) and (h.age<=32)]
print(f)
# [('Alice', 29), ('Bob', 32), ('Daphne', 30), ('David', 31)]
print("\n-----------------------------------------------\n")

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(h.name.upper(), h.age + 5) for h in humans]
print(g)
# [<Human: ALICE, 34>, <Human: BOB, 37>, <Human: CHARLIE, 42>, <Human: DAPHNE, 35>, <Human: EVE, 31>, <Human: FRANK, 23>, <Human: GLENN, 47>, <Human: HARRISON, 17>, <Human: IGON, 46>, <Human: DAVID, 36>]
print("\n-----------------------------------------------\n")

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(h.age) for h in humans]
print(h)
# [5.385164807134504, 5.656854249492381, 6.082762530298219, 5.477225575051661, 5.0990195135927845, 4.242640687119285, 6.48074069840786, 3.4641016151377544, 6.4031242374328485, 5.5677643628300215]
print("\n-----------------------------------------------\n")