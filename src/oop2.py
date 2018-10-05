 class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels
    def drive(self):
        print("vroooom")




# Subclass Motorcycle from Vehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __intit__(self):
        super().__init__(2)
    def drive(self):
        print("BRAAAP!!")

# TODO
# moto = Motorcycle()
# moto.drive()


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

for vehicle in vehicles:
    vehicle.drive()
