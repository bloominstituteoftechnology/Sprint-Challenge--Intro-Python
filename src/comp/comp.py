# The following list comprehension exercises will make use of the 
# defined Human class. 
import math
from collections import namedtuple
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
[a.append((str(v)[:-5][8:])) for v in humans if "Human: D" in str(v) ]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
[b.append((str(v)[:-5][8:])) for v in humans if "e," in str(v) ]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
[c.append((str(v)[:-5][8:])) for v in humans if "Human: C" in str(v) or "Human: D" in str(v) or "Human: E" in str(v) or "Human: F" in str(v) or "Human: G" in str(v) ]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
[d.append(int(str(v)[-3:-1])+10) for v in humans if True ]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
[e.append(str(v).replace("<Human: ","").replace('>','').replace(', ','-') ) for v in humans if True ]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
[f.append((str(v)[:-5][8:],int(str(v)[-3:-1])) ) for v in humans if int(str(v)[-3:-1]) > 26 and int(str(v)[-3:-1]) < 33  ]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
Human = namedtuple("Human",'name age')
[g.append(Human(str(v)[:-5][8:].upper(),(int(str(v)[-3:-1])+5 ))) for v in humans if True  ]
print(str(g).replace("name='",'"').replace("', age=",'", '))

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
[h.append(math.sqrt(int(str(v)[-3:-1]))) for v in humans if True ]
print(h)
