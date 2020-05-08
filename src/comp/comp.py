#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The following list comprehension exercises will make use of the 
# defined Human class. 
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


# In[2]:


# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [h.name for h in humans if h.name[0]=='D']
print(a)


# In[3]:


# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [h.name for h in humans if h.name[-1]=='e']
print(b)


# In[4]:


# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [h.name for h in humans if h.name[0] in ['C','D','E','F','G']]
print(c)


# In[5]:


# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [h.age + 10 for h in humans]
print(d)


# In[6]:


# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = d = [h.name + '-' + str(h.age) for h in humans]
print(e)


# In[7]:


# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(h.name, h.age) for h in humans if h.age in range(27,32 + 1)]
print(f)


# In[8]:


# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")

# ulclear
#g = [(h.name.upper(), h.age+5) for h in humans if h.age in range(27,32 + 1)]
#or
g = [(h.name.upper(), h.age+5) for h in humans]
print(g)


# In[9]:


# Write a list comprehension that contains the square root of all the ages.

# Pedantic: I interpret this to mean square roots of EACH age, and the desired 
# output to be a list of the square root of each age

# Write a list comprehension that contains the square root of all the ages.
print("Square roots of ages:")
import math
h = [math.sqrt(h.age) for h in humans]
print(h)


# If we only want the one square root of (the sum of) all the ages:
# h = [h.age for h in humans]
# h_sum = sum(h)
# h_sum_sqrt = math.sqrt(h_sum)
# # print(h_sum_sqrt)
# h_sum_sqrt_list = [h_sum_sqrt]
# print(f"Square root of sum of ages as a one-element list: {str(h_sum_sqrt_list)}")


# In[ ]:




