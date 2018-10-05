class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)

humans = {
    "Alice": Human("Alice", 29),
    "Bob": Human("Bob", 32),
    "Charlie": Human("Charlie", 37),
    "Daphne": Human("Daphne", 30),
    "Eve": Human("Eve", 26),
    "Frank": Human("Frank", 18),
    "Glenn": Human("Glenn", 42),
    "Harrison": Human("Harrison", 12),
    "Igon": Human("Igon", 41),
    "David": Human("David", 31),
}



# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

# for i in Human():
#     print(i)

# print("Starts with D:")
r = []  
# TODO
for each in humans:
    if "D" in each:
        r.append(each)

print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = []  
# TODO
for each in humans:
    if "e" in each[len(each) - 1]:
        r.append(each)

print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = []  # TODO

for each in humans:
    if "C" == each[0] or "D" == each[0] or "E" == each[0] or "F" == each[0] or "G" == each[0]:
        r.append(each)

print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = []  # TODO

for each in humans:
    print(Human.name)

print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = []  # TODO
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = []  # TODO
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The `humans` list should be unmodified.
print("All names capitalized:")
r = []  # TODO
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []  # TODO
print(r)