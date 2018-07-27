# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels

    # TODO

    def drive(self):
        print("vroooom")

    def default_wheels(self, num_wheels):
        if num_wheels == None:
            num_wheels = 4


# Subclass Motorcycle from Vehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(2)

    def drive(self):
            print("BRAAAP!!")

vehicles = [
    GroundVehicle(4),
    GroundVehicle(4),
    Motorcycle(),
    GroundVehicle(4),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

# TODO
print(vehicles[0].drive())
print(vehicles[1].drive())
print(vehicles[2].drive())
print(vehicles[3].drive())
print(vehicles[4].drive())
print(vehicles[5].drive())
