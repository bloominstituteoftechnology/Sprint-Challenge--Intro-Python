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
    # base class
    def __init__(self, name):
        self.name
    pass

class GroundVehicle(Vehicle):
    def __init__(self, name):
        self.name
    pass

class Car(GroundVehicle):
    def __init__(self, name):
        self.name
    pass

class Motorcycle(GroundVehicle):
    def __init__(self, name):
        self.name
    pass

class FlightVehicle:
    def __init__(self, name):
        self.name
    pass

class Airplane(FlightVehicle):
    def __init__(self, name):
        self.name
    pass

class Starship:
    def __init__(self, name):
        self.name
    pass






