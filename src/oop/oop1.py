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
# base class -- vehicle

class Vehicle:
    '''base class'''
    pass


class GroundVehicle(Vehicle):
    ''' sub-class of vehicle'''
    pass


class Car(GroundVehicle):
    '''sub-class of GroundVehicle'''
    pass


class Motorcycle(GroundVehicle):
    '''sub-class of GroundVehicle'''


class FlightVehicle(Vehicle):
    '''sub-class of Vehicle'''
    pass


class Airplane(FlightVehicle):
    '''sub-class of FlightVehicle'''
    pass


class Starship(FlightVehicle):
    '''sub-class of FlightVehicle'''
    pass