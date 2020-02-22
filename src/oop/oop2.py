# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
    def __init__(self):
        self.num_wheels = 4
    def drive(self):
        return "vroooom"

    # TODO

# car = GroundVehicle()

# print(car.drive())
# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    pass
    def __init__(self):
        self.num_wheels = 2
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

# TODO
print(vehicles[0].drive())
print(vehicles[1].drive())
print(vehicles[2].drive())
print(vehicles[3].drive())
print(vehicles[4].drive())
