# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels
        # if num_wheels is None:
        # num_wheels = 4
    def drive(self):
        print("vroooom")    
        

    # TODO
class Motorcycle(GroundVehicle):
    def __init__(self):
        GroundVehicle.__init__(self, 2 )
    def drive(self):
        print("BRAAAP!!")
# Subclass Motorcycle from Vehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle(4),
    GroundVehicle(5),
    Motorcycle(),
    GroundVehicle(6),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

r = [i.drive() for i in vehicles]  
print(r)
# TODO
