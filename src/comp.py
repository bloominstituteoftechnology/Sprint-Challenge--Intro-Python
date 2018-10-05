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

# loop through each human
# if name starts with D
# print Name
# else pass

print("Starts with D:")

r = []  # TODO

for hum in humans:
    s = list(hum.name)
    # print(s)
    if s[0] != "D":
        continue
    r.append(hum.name)
print(f"{r}\n")


# # Write a list comprehension that creates a list of names of everyone
# # whose name ends in "e".

print("Ends with e:")
r = []  # TODO
for hum in humans:
    s = list(hum.name)
    # print(s)
    if s[-1] != "e":
        continue
    r.append(hum.name)
print(f"{r}\n")



# # Write a list comprehension that creates a list of names of everyone
# # whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = []  # TODO
# letters = ["C","D","E","F","G"]

for hum in humans:
    s = list(hum.name)
    for i in s[0]:
        if "C" <= s[0] <= "G":
            r.append(hum.name)
            # print(r)
# print(r)


print(f"{r}\n")



# # Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = []  # TODO

for hum in humans:
    r.append(hum.age + 10) 


print(f"{r}\n")




# # Write a list comprehension that creates a list of strings which are the name
# # joined to the age with a hyphen, for example "David-31", for all humans.

print("Name hyphen age:")
r = []  # TODO

for hum in humans:
    r.append(f"{hum.name}-{hum.age}")

print(f"{r}\n")


# # Write a list comprehension that creates a list of tuples containing name and
# # age, for example ("David", 31), for everyone between the ages of 27 and 32,
# # inclusive.
print("Names and ages between 27 and 32:")
r = []  # TODO

for hum in humans: 
    if  32 >= hum.age >= 27:
        r.append((str(hum.name), hum.age))

print(f"{r}\n")


# # Write a list comprehension that creates a list of new Humans like the old
# # list, except with all the names capitalized and the ages with 5 added to them.
# # The `humans` list should be unmodified.
print("All names capitalized:")
r = []  # TODO
for hum in humans:
    r.append((hum.name.upper(), hum.age + 5))

print(f"{r}\n")


# # Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []  # TODO
for hum in humans:
    r.append(math.sqrt(int(hum.age)))
print(r)