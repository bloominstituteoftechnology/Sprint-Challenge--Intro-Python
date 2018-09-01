# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

# class GroundVehicle():
#     def __init__(self, num_wheels):
#         self.num_wheels = num_wheels

#     # TODO
class GroundVehicle(Vehicle):
    def __init__(self, name, num_wheels=None):
        super().__init__(name)
        self.type = "ground"
        self.num_wheels = num_wheels
    def drive(self):
        print("vroooom")

class Car(GroundVehicle):
    def __init__(self, name, num_wheels=4):
        super().__init__(name, num_wheels)

t = Car("Toyota")


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO
class Motorcycle(GroundVehicle):
    def __init__(self, name, num_wheels=2):
        super().__init__(name, num_wheels)
    def drive(self):
        print("BRAAAP!!")

n = Motorcycle("Triumph")

# vehicles = [
#     GroundVehicle(),
#     GroundVehicle(),
#     Motorcycle(),
#     GroundVehicle(),
#     Motorcycle(),
# ]

vehicles = [
    GroundVehicle("McLaren"),
    GroundVehicle("Reliant", 3),
    Motorcycle("Triumph"),
    GroundVehicle("Mercedes G63 AMG 6x6", 6),
    Motorcycle("Harley-Davidson Freewheeler", 3),
]

# Go through the vehicles list and call drive() on each.

# TODO
for vehicle in vehicles:
    vehicle.drive()
