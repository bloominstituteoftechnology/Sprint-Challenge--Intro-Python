#bring in math for sqrt()
import math

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)

#names list to hold names
names = []

#ages list to hold ages
ages = []

#both array
both = []

startsWith = ["C", "D", "E", "F", "G"]

#fill this array with ages 27-32 for below function
ageLim = []

cAndG = []

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

#fill names list 
names.append(humans[0].name)
names.append(humans[1].name)
names.append(humans[2].name)
names.append(humans[3].name)
names.append(humans[4].name)
names.append(humans[5].name)
names.append(humans[6].name)
names.append(humans[7].name)
names.append(humans[8].name)
names.append(humans[9].name)

# fill ages list
ages.append(humans[0].age)
ages.append(humans[1].age)
ages.append(humans[2].age)
ages.append(humans[3].age)
ages.append(humans[4].age)
ages.append(humans[5].age)
ages.append(humans[6].age)
ages.append(humans[7].age)
ages.append(humans[8].age)
ages.append(humans[9].age)

#both variables to populate array
Alice = str(humans[0].name) + "-" + str(humans[0].age)
Bob = str(humans[1].name) + "-" + str(humans[1].age)
Charlie = str(humans[2].name) + "-" + str(humans[2].age)
Daphne = str(humans[3].name) + "-" + str(humans[3].age)
Eve = str(humans[4].name) + "-" + str(humans[4].age)
Frank = str(humans[5].name) + "-" + str(humans[5].age)
Glenn = str(humans[6].name) + "-" + str(humans[6].age)
Harrison = str(humans[7].name) + "-" + str(humans[7].age)
Igon = str(humans[8].name) + "-" + str(humans[8].age)
David =str(humans[9].name) + "-" + str(humans[9].age)

both.append(Alice)
both.append(Bob)
both.append(Charlie)
both.append(Daphne)
both.append(Eve)
both.append(Frank)
both.append(Glenn)
both.append(Harrison)
both.append(Igon)
both.append(David)

ageLim.append(Bob)
ageLim.append(Daphne)
ageLim.append(Eve)
ageLim.append(Frank)

#fill C and G array for below 
cAndG.append(humans[2].name)
cAndG.append(humans[3].name)
cAndG.append(humans[4].name)
cAndG.append(humans[5].name)
cAndG.append(humans[6].name)
cAndG.append(humans[9].name)





#print both lists to check contents
print("\n\n")
print(f'Names list:  {names}')
print(f'Ages list:  {ages}')
print(f'Both list: {both}')
print(f'AgeLim list: {ageLim}')
print("\n\n")


# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
r = [name for name in names if name.startswith("D")]  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = [name for name in names if name.endswith("e")]  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = [name for name in cAndG]  # TODO
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = [age for age in ages if age > 10]  # TODO
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = [both for both in both]  # TODO
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = [names for names in ageLim]  # TODO
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
r = [name.capitalize() for name in names]  # TODO
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = [math.sqrt(age) for age in ages]  # TODO
print(r)