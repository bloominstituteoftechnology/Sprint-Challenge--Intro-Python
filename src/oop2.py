# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, name="Ground Vehicle", num_wheels=4):
        self.name = name
        self.num_wheels = num_wheels

    def drive(self):
        print("vroooom")

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, name="Motorcycle", num_wheels=2):
        GroundVehicle.__init__(self, name, num_wheels)
    def drive(self):
        print("BRAAAP")


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

print(f"{vehicles[0].name} has {vehicles[0].num_wheels} wheels.")
vehicles[0].drive()

print(f"{vehicles[1].name} has {vehicles[1].num_wheels} wheels.")
vehicles[1].drive()

print(f"{vehicles[2].name} has {vehicles[2].num_wheels} wheels.")
vehicles[2].drive()

print(f"{vehicles[3].name} has {vehicles[3].num_wheels} wheels.")
vehicles[3].drive()

print(f"{vehicles[4].name} has {vehicles[4].num_wheels} wheels.")
vehicles[4].drive()