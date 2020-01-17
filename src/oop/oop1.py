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
    '''This is a super class and base class'''
    pass

class FlightVehicle(Vehicle):
    '''Super class to Airplane but subclass of Vehicle'''
    pass

class Starship(FlightVehicle):
    '''Subclass of flight vehicle'''
    pass

class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class Airplane(FlightVehicle):
    pass
