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

# Base Class

class Vehicle:

    def __init__(self, type):
        self.type = type

# Vehicle Types

class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass

# Flight Vehicle Types

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

# Ground Vehicle Types

class Car(GroundVehicle):
    pass

class Motorcylce(GroundVehicle):
    pass