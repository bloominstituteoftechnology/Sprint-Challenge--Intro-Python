# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=None):
        if num_wheels != None:
            self.num_wheels = num_wheels
            
        else:
            num_wheels = 4

    def drive(self):
        print("vroooom")


# Subclass Motorcycle from Vehicle.

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        GroundVehicle.__init__(self, num_wheels)

    def drive(self):
        print("BRAAP!!")
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(2),
    GroundVehicle(),
    Motorcycle(2),
]

# Go through the vehicles list and call drive() on each.

vehicles[0].drive()
vehicles[1].drive()
vehicles[2].drive()
vehicles[3].drive()
vehicles[4].drive()
