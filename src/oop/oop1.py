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
    """
    Base Class
    """
    pass


class GroundVehicle(Vehicle):
    """
    From Vehicle
    """
    pass


class Car(GroundVehicle):
    """
    From Ground Vehicle
    """
    pass


class Motorcycle(GroundVehicle):
    """
    From Ground Vehicle
    """
    pass


class FlightVehicle(Vehicle):
    """
    From Vehicle
    """
    pass


class Starship(FlightVehicle):
    """
    From FlightVehicle
    """
    pass


class Airplane(FlightVehicle):
    """
    From FlightVehicle
    """
    pass
