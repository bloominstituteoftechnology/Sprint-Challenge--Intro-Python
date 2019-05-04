# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels: int = 4):
        self.num_wheels = num_wheels

    def drive(self):
        return f'vroooom'


# Subclass Motorcycle from GroundVehicle.

# GroundVehicle is base class
class Motorcycle(GroundVehicle):
    """ This is a Motorcycle Class """
    # Make it so when you instantiate a Motorcycle, it automatically sets the number
    # of wheels to 2 by passing that to the constructor of its superclass.
    def __init__(self, num_wheels: int = 2, includesComplementaryLeatherJacket: bool = True):
        super().__init__(num_wheels=num_wheels)
        self.includesComplementaryLeatherJacket = includesComplementaryLeatherJacket

    # Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
    def drive(self):
        return f'BRAAAP!!'

    def __str__(self):
        return str(self.__dict__)

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

[print(n.drive()) for n in vehicles]