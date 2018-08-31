# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
from oop1 import Vehicle

class GroundVehicle(Vehicle):
    def __init__(self, num_wheels=4):
        Vehicle.__init__(self)
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        print('vroooom')

# Subclass Motorcycle from Vehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO
class Motorcycle(Vehicle):
    def __init__(self, num_wheels=2):
        Vehicle.__init__(self, num_wheels)

    def drive(self):
        print('BRAAAPP!!')

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

# TODO
for vehicle in vehicles:
    vehicle.drive()

# list(map(lambda x: x.drive(), vehicles))