# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


class GroundVehicle():
    def __init__(self):
        self.num_wheels = 4

    def drive(self):
        return "vroooom"


class Motorcycle(GroundVehicle):
    def __init__(self):
        self.num_wheels = 2

    def drive(self):
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

for car in vehicles:
    print(car.drive)
