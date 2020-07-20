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
    '''Base class'''
    pass
class GroundVehicle (Vehicle):
    '''Subclass of Parent class Vehicle'''
    pass
class FlightVehicle (Vehicle):
    '''Subclass of Parent class Vehicle'''
    pass
class Starship (FlightVehicle):
    '''Subclass of Parent class F lightVehicle'''
    pass
class Airplane (FlightVehicle):
    '''Subclass of Parent class FlightVehicle'''
    pass
class Car (GroundVehicle):
    '''Subclass of GroundVehicle'''
    pass
class Motorcycle (GroundVehicle):
    '''subclass of GroundVehicle'''
    pass
