"""
Modified versions of the GroundVehicle and Motorcycle classes, with 
additional methods and attributes.
"""


# Import libraries, modules, functions:
from oop1 import Vehicle


# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
class GroundVehicle(Vehicle):
    """
    Representation of a specialized type of Vehicle object that only operates 
    on the ground.
    """
    def __init__(self, num_wheels = 4):
        super().__init__()
        self.num_wheels = num_wheels

    def drive(self):
        """
        Drive the vehicle. Returns "vroooom" always.
        """
        return "vroooom"

# Subclass Motorcycle from GroundVehicle:
# (1) Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
# (2) Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
class Motorcycle(GroundVehicle):
    """
    Representation of a specialized type of GroundVehicle object that carries 
    passengers and has 2 wheels.
    """
    def __init__(self, num_wheels = 2):
        super().__init__(num_wheels=num_wheels)
        pass

    def drive(self):
        """
        Drive the motorcycle. Returns "BRAAAP!!" always.
        """
        return "BRAAAP!!"

# Make a list of newly-created ground vehicles:
vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
print(*[vehicle.drive() for vehicle in vehicles])  # If separators needed: print(*[...], sep = ", ")

# # Alternative syntax to print on separate lines:
# for vehicle in vehicles:
#     print(vehicle.drive())
