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
for each in humans:
    if each.name[:1] == "D":
        r = []
        r.append(each)
    else:
        pass

print("Starts with D:")
  # TODO
print(r)


# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
v = []   
for each in humans:
    if each.name[-1] == "e":     
        v.append(each)
    else:
        # print(each.name[-1])
        pass

print("Ends with e:")
# TODO
print(v)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
j = []  # TODO
for each in humans:
    for c in range(ord('C'), ord('G')+1):
        if each.name[:1] == chr(c):
            j.append(each)
        else:
            pass

print(j)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
k = []  # TODO
for each in humans:
    if each.age:
        bob = each.age
        bob += 10
        k.append(bob)
    else:
        pass
print(k)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
g = []  # TODO
for each in humans:
    if each.age:
        bob = str(each.name) + '-' + str(each.age)
        g.append(bob)
    else:
        pass
print(g)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = []  # TODO
for each in humans:
        if each.age >= 27 and each.age <= 32:
            r.append(each)
        else:
            pass
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
r = []  # TODO
for each in humans:
    bob = str(each.name.upper()) + ", "+ str(each.age +5)
    r.append(bob)
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []  # TODO
for each in humans:
    if each.age:
        bob = math.sqrt(each.age)
        r.append(bob)
    else:
        pass
print(r)