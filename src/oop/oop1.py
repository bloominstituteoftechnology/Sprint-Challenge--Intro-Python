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
    """Base class of all vehicles"""
    pass


class FlightVehicle(Vehicle):
    '''Parent class for flying vehicles.
       Base class is Vehicle'''
    pass


class Starship(FlightVehicle):
    '''Starship class - base is Vehicle'''
    pass


class Airplane(FlightVehicle):
    '''Airplane class - base is Vehicle'''
    pass


class GroundVehicle(Vehicle):
    '''Parent class for ground vehicles.
       Base class is Vehicle'''
    pass


class Car(GroundVehicle):
    '''Car class - base is Vehicle'''
    pass


class Motorcycle(GroundVehicle):
    '''Motorcycle class - base is Vehicle'''
    pass
