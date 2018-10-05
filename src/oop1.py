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


class Vehicle():
    def __init__(self, name):
        self.name = name


class GroundVehicle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)


class Car(GroundVehicle):
    def __init__(self, name):
        GroundVehicle.__init__(self, name)


class Motorcycle(GroundVehicle):
    def __init__(self, name):
        GroundVehicle.__init__(self, name)


class FlightVehicle(Vehicle):
    pass


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass
