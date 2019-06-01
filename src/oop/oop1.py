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
    pass


class FlightVehicle(Vehicle):
    # Base class is Vehicle
    pass


class Starship(FlightVehicle):
    # Base class is FlightVehicle
    pass


class Airplane(FlightVehicle):
    # Base class is FlightVehicle
    pass


class GroundVehicle(Vehicle):
    # Base class is Vehicle
    pass


class Car(GroundVehicle):
    # Base class is GroundVehicle
    pass


class Motorcycle(GroundVehicle):
    # Base class is GroundVehicle
    pass
