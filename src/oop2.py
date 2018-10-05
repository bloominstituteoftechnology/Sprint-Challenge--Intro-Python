# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
num_wheels = 0

if num_wheels is 0 or "":
    print(4)  
else:
    print(num_wheels)


class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        print("vroooom")

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO
class Motorcycle(GroundVehicle):
    def __init__(self):
        self.num_wheels = 2
    
    def drive(self):
        print("BRAAAP!!")



vehicles = [
    GroundVehicle(4),
    GroundVehicle(3),
    Motorcycle(),
    GroundVehicle(6),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

# TODO

GroundVehicle.drive("drive")
GroundVehicle.drive("drive")
Motorcycle.drive("drive")
GroundVehicle.drive("drive")
Motorcycle.drive("drive")