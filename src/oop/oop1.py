# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():
    pass

class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return 'vroooom'

class Car(GroundVehicle):
    def __init__(self):
        super().__init__(num_wheels=4)

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(num_wheels=2)

    def drive(self):
        return 'BRAAAP!!'

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass