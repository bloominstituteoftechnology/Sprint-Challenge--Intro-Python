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
    '''This is the base class'''
    pass


class FlightVehicle(Vehicle):  # this inherits from the base class Vehicle
    pass


class Airplane(FlightVehicle):  # this class inherits from FlightVehicle
    pass


class Starship(FlightVehicle):  # this class inherits from FlightVehicle
    pass


class GroundVehicle(Vehicle):  # this inherits from the base class Vehicle
    pass


class Car(GroundVehicle):  # this class inherits from GroundVehicle
    pass


class Motorcycle(GroundVehicle):  # this class inherits from GroundVehicle
    pass
