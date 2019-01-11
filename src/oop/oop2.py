# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
import sys
DEFAULT = object()


class GroundVehicle():
    def __init__(self, num_wheels=DEFAULT):
        # Checks if num_wheels is set to None then assigns 4
        if num_wheels is DEFAULT:
            self.num_wheels = 4
        # If num_wheels exists assigns num_Wheels to self.num_wheels
        else:
            self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


class Motorcycle(GroundVehicle):
    def __init__(self):
        self.num_wheels = 2
        super().__init__(self)

    def drive(self):
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    print(vehicle.drive())
