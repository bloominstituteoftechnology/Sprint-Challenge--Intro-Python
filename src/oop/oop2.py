# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, drive, num_wheels):
        self.num_wheels = num_wheels
        self.drive = "vroooom"
        self.num_wheels = 4

    # TODO
    def __str__(self):
        return self.drive


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO
class Motorcycle(GroundVehicle):
    def __init__(self):
        self.num_wheels = 2
        self.drive = "BRAAAP!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

my_vehicle = Vehicle({self.drive})
print(my_vehicle)

# TODO
