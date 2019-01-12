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


class Vehicle(object):
    pass


class GroundVehicle(Vehicle):
    pass
# baseclass Vehicle


class Car(GroundVehicle):
    pass
# baseclass GroundVehicle


class Motorcycle(GroundVehicle):
    pass
# baseclass GroundVehicle


class FlightVehicle(Vehicle):
    pass
# baseclass Vehicle


class Airplane(FlightVehicle):
    pass
# baseclass FlightVehicle


class StarShip(FlightVehicle):
    pass
# baseclass FlightVehicle
