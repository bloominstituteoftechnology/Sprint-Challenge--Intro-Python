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

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

print("Starts with D:")
r = []  # TODO
for each in humans:
    if each.name[0] == "D":
        r.append(each.name)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = []  # TODO
for each in humans:
    if each.name[-1] == "e":
        r.append(each.name)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = []  # TODO
for each in humans:
    for c_compare in xrange(ord('C'), ord('G')+1):
        if ord(each.name[0]) == c_compare:
            r.append(each.name)
    
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = []  # TODO
for each in humans:
    r.append(each.age + 10)
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = []  # TODO
for each in humans:
    concat = each.name + '-' + str(each.age)
    r.append(concat)
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = []  # TODO
for each in humans:
    if each.age >= 27 and each.age <=32:
        tuple_age = (each.name, each.age)
        r.append(tuple_age)
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
r = []  # TODO
new_h_list = []
for each in humans:
    new_humans = Human(each.name.upper(), each.age + 5)
    new_list = [each.name.upper(), each.age + 5]
    r.append(new_humans)
    new_h_list.append(new_list)
print(r)
# print(new_h_list)


# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []  # TODO
for each in humans:
    r.append(math.sqrt(each.age))
print(r)