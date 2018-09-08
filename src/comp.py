import math

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

print(humans)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

print("Starts with D:")
r = []  # TODO
for arr in humans:
    for attr, value in arr.__dict__.items():
            if type(value) is  str and value[0] == "D": 
                r.append(value)

print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = []  # TODO
for arr in humans:
    for attr, value in arr.__dict__.items():
            if type(value) is  str and value[-1] == "e": 
                r.append(value)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = []  # TODO
for arr in humans:
    for attr, value in arr.__dict__.items():
            # if type(value) is  str and (value[0]== "C" or value[0] == "D" or value[0] == "E" or value[0] == "F" or value[0] == "G"): 
            if type(value) is  str and (value.startswith(("C", "D", "E", "F", "G"))): #startswith --> tuple , str
                r.append(value)

print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = []  # TODO
for arr in humans:
    for attr, value in arr.__dict__.items():
            # if type(value) is  str and (value[0]== "C" or value[0] == "D" or value[0] == "E" or value[0] == "F" or value[0] == "G"): 
            if type(value) is  int:
                r.append(value + 10)
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = []  # TODO
for arr in humans:
    r.append(arr.name+"-"+ str(arr.age))
     
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = []  # TODO
for arr in humans:
    if arr.age in range(27,32):
        temp = (arr.name,arr.age)
        r.append(temp)
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The `humans` list should be unmodified.
print("All names capitalized:")
r = []  # TODO
for arr in humans:
    temp = Human(arr.name.capitalize(), arr.age + 5)
    r.append(temp)
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []  # TODO
for arr in humans:
    r.append(math.sqrt(arr.age))
print(r)