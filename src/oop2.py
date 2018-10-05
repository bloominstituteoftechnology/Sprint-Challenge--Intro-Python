# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = 4
    def drive(self, vehicle):
        print("VROOOOOOOOOOOOOOOOOOOOM")
   


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        self.num_wheels = 2
    def drive(self, vehicle):
        print("BRAAAAAAAAAAAAAAP")

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

vehicle.drive()
GroundVehicle(vehicles.drive())
Motorcycle(vehicles.drive())
vehicle.GroundVehicle.drive()
vehicle.Motorcycle.drive()
GroundVehicle