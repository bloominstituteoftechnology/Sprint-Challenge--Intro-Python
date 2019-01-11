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
# base class Vehicle


class Car(GroundVehicle):
    pass
# base class GroundVehicle


class Motorcycle(GroundVehicle):
    pass
# base clasee GroundVehicle
