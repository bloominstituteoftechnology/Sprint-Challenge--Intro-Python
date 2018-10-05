# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels, drive):
        self.num_wheels = 4
    def drive(self):
        print("vrooom")

    # TODO


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels, drive):
        GroundVehicle.__init__(self, num_wheels, drive):
            super().__init__(num_wheels, drive)
            self.num_wheels: 2
    def drive(self):
        print("BRAAP")
# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

for attr in vehicles:
    attr.drive()
# TODO
