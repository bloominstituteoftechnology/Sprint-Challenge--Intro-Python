# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = 4
    def drive(self):
        print("vroooom")
    # TODO


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        GroundVehicle.__init__(self, num_wheels)
        self.num_wheels = 2
    def drive(self):
        print("BRAAAP!!")

vehicles = [
    GroundVehicle(vehicle, 4),
    GroundVehicle(vehicle, 4),
    Motorcycle(vehicle, 2),
    GroundVehicle(vehicle, 4),
    Motorcycle(vehicle, 2),
]

# Go through the vehicles list and call drive() on each.

for i in vehicles:
    vehicles[i].drive(vehicle)


# TODO
