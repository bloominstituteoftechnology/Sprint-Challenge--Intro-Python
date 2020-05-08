# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class Vehicle:
    pass

class GroundVehicle(Vehicle):
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by 
# !!! passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        self.num_wheels = num_wheels

    def drive(self):
        return "BRAAAP!!"
# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.


# my_harley = Motorcycle()

# print(my_harley.num_wheels)

# Go through the vehicles list and print the result of calling drive() on each.

for v in vehicles:
    print(v.drive())
# [print(v.drive()) for v in vehicles]
