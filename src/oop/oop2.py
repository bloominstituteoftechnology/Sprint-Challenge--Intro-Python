# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

    def drive(self):
        return("vroooom")

    # TODO


# Subclass Motorcycle from GroundVehicle.

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        self.num_wheels = num_wheels

    def drive(self):
        return("BRAAAP!!")
        
        

#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

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
