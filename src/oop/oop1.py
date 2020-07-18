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

class Vehicle:
    def __init__(self, name, orientation):
        self.name = name
        self.orientation

class GroundVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name, orientation)

class Car(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)

class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)

class FlightVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name, orientation)

class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)

class Starship(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)


