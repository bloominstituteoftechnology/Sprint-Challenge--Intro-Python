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

# Base Class Vehicle


class Vehicle:
    def __init__(self):
        pass

# inherits class Vehicle


class FlightVehicle(Vehicle):
    def __init__(self):
        pass
# inherits FlightVehicle class


class Starship(FlightVehicle):
    def __init__(self):
        pass
# inherits class Vehicle


class GroundVehicle(Vehicle):
    def __init__(self):
        pass
# inherits FlightVehicle class


class Airplane(FlightVehicle):
    def __init__(self):
        pass
# inherits GroundVehicle class


class Car(GroundVehicle):
    def __init__(self):
        pass
# inherits GroundVehicle class


class Motorcycle(GroundVehicle):
    def __init__(self):
        pass
