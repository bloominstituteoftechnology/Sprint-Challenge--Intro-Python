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

#Test how to get names
print(type(humans))
# <class 'list'>

# for k, v in humans:
#     print(k)
# # cannot unpack non-iterable Human object

#try name
for h in humans:
    print(h.name)

#Answer
# [Alice
# Bob
# Charlie
# Daphne
# Eve
# Frank
# Glenn
# Harrison
# Igon
# David]

a = []

#Create for loop
# for h in humans:
#     if h.name[0]== "D":
#         a.append(h.name)

# list_comprehension = "expression for item in list"
# https://www.programiz.com/python-programming/list-comprehension

#Turn to list comprehension
print("Starts with D:")
a = [h.name for h in humans if h.name[0] == "D"]
print(a)

# This works
# include = ["C", "D", "E", "F", "G"]

#still works
print("Starts between C and G, inclusive:")
c = [h.name for h in humans if h.name[0] in ("C", "D", "E", "F", "G")]
print(c)

print("Ages plus 10:")
d = [h.age + 10 for h in humans]
print(d)

#Did not work?
# Need to make into f string
print("Name hyphen age:")
e = [f"{h.name}-{h.age}" for h in humans]
print(e)

print("Names and ages between 27 and 32:")
f = [(h.name, h.age) for h in humans if (h.age >=27) and (h.age<=32)]
print(f)

print("All names uppercase and age + 5:")
g = [Human(h.name.upper(), h.age + 5) for h in humans]
print(g)