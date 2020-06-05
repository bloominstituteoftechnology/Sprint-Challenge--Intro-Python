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

#for the record, I would prefer regex there
# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

comp_D = [d for d in humans if human[0] == "D" ]
print("Starts with D:")
d = []
print(d)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

#comp_E = [e for e in range(len(humans)) if e starts with E]
comp_D = [e for e in humans if human[0] == "e" ]
print("Ends with e:")
e = []
print(e)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
#comp_CG = [c for c in range(len(humans)) if c has either letter C or G]
comp_CG = [c for c in humans if human[0] == "c" if human[0] == "g" ]
print("Starts between C and G, inclusive:")
c = []
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
#lambda function thought
comp_age = [age for age in range(len(humans)) if age + 10]
print("Ages plus 10:")
age = []
print(age)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
comp_join = [join for join in range(len(join)) if name hyphen number]
print("Name hyphen age:")
join = []
print(join)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
#comp_old = [old for old in range(len(humans)) if ages are between 27 and 32]
comp_old = [old for old in range(len(humans)) if old >= 27 and <= 32]
print("Names and ages between 27 and 32:")
old = []
print(old)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
comp_proper = [pro.upper() and pro + 5 for pro in range(len(humans))]
print("All names uppercase:")
pro = []
print(pro)

# Write a list comprehension that contains the square root of all the ages.
comp_sqr = [sqr**2 for sqr in range(len(humans))]
print("Square root of ages:")
import math
sqr = []
print(sqr)

#
#{x:[i for i,sen in enumerate(list6) if any(x==item for item in sen.split())] for x in list5}
#{'apple': [0, 3, 4], 'mango': [2, 5], 'sherbet': []}
