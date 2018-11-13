class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)

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
r = [char.name for char in humans]  
d_list = [word for word in r if word[0] == "D"]
print(d_list)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = [char.name for char in humans]  
e_end = [word for word in r if word[-1] == 'e']
print(e_end)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = [char.name for char in humans]  
first_letters = ["C", "D", "E", "F", "G"]
cg_names = [name for name in r if (name[0] in first_letters)]
print(cg_names)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = [peeps.age for peeps in humans]  
ten = [age * 10 for age in r]
print(ten)
# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = []  # TODO
for human in humans:
    r.append(human.name+"-"+str(human.age))
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = [peeps.age for peeps in humans if (peeps.age < 32) & (peeps.age > 27)]  
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The `humans` list should be unmodified.
print("All names capitalized:")
r = []
for human in humans:
    r.append((str.upper(human.name),(human.age+5)))
print()
# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []
for human in humans:
    r.append(human.age**2)
print(r)