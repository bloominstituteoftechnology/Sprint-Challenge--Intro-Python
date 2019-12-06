# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

    # TODO
    def drive(self): # method
        return ("vroooom") #Must return the string instead of just printing it. Otherwise is prints as a nontype!
    
    def __repr__(self):
        return f'({repr(self.num_wheels)})'

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        self.num_wheels = num_wheels

    def drive(self): # method
        return ("BRAAAP!!") #Must return the string instead of just printing it. Otherwise is prints as a nontype!

    def __repr__(self):
        return f'({repr(self.num_wheels)})'


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

def sound(vehicle):
 
    for v in vehicle:
        v.drive()

    return vehicle

    
# type(sound(vehicles)) # --> used to debug why there was an assertionerror of none
print(sound(vehicles))
