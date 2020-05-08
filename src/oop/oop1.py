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
    def __init__(self):
        '''this is the base class of vehicles'''
        pass


class FlightVehicle(Vehicle):
    def __init__(self):
        '''this is the intermediary class for flying vehicles'''
        pass


class Starship(FlightVehicle):
    def __init__(self):
        '''used for flying to other worlds through deep space'''
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        '''Can be used for cargo or passengers for high speed transport around
        the globe'''
        pass


class GroundVehicle(Vehicle):
    def __init__(self):
        '''an intermediary class for vehicles that travel on land'''
        pass


class Car(GroundVehicle):
    def __init__(self):
        '''the most common way to get around the United States'''
        pass


class Motorcycle(GroundVehicle):
    def __init__(self, cool_factor=10):
        '''a special driving vehicles mostly used for its high cool factor of getting around'''
        self.cool_factor = cool_factor
