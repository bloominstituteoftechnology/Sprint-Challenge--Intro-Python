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

print("\nStarts with D:")
r = [each for each in humans if each.name[0] == "D"]  # TODO
print(r)
# D names print successfully to terminal (Daphne & David)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("\nEnds with e:")
r = [each for each in humans if each.name[-1] == "e"]  # TODO
print(r)
# Names ending in 'e' print successfully to terminal (Alice, Charlie, Daphne & Eve)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("\nStarts between C and G, inclusive:")
r = [each for each in humans if each.name[0] >= "C" and each.name[0] <= "G"]  # TODO
print(r)
# Names the start with letters C, D, E, F, or G print successfully to terminal (Charlie, Daphne, Eve, Frank, Glenn & David) 

# Write a list comprehension that creates a list of all the ages plus 10.
print("\nAges plus 10:")
r = [each.age + 10 for each in humans]  # TODO
print(r)
# All ages (+10) print successfully to the terminal

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("\nName hyphen age:")
r = ["-".join([each.name, str(each.age)]) for each in humans]  # TODO
print(r)
# All names joined with their ages ('name-age') print successfully to the terminal

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("\nNames and ages between 27 and 32:")
r = [each for each in humans if each.age >= 27 and each.age <= 32]  # TODO
print(r)
# All names between the ages of 27 and 32 print successfully to terminal

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("\nAll names capitalized:")
r = [list(map(lambda x: Human(x.name.upper(), x.age + 5), humans))]  # TODO
print(r)
# All names print uppercased and all ages have +5 added to them and successfully prints to terminal

# Write a list comprehension that contains the square root of all the ages.
print("\nSquare root of ages:")
r = [each.age ** 0.5 for each in humans]  # TODO
print(r)
# All square root of ages prints successfully to terminal