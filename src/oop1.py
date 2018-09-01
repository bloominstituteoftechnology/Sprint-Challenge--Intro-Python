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
    """Base Class"""
    def __init__(self, name):
        self.name = name
        self.base = "vehicle"



class GroundVehicle(Vehicle):
    """secondary base"""
    def __init__(self, name):
        super().__init__(name)
        self.type = "ground"

class Car(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)

class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)


class FlightVehicle(Vehicle):
    """secondary base"""
    def __init__(self, name):
        super().__init__(name)
        self.type = "air"

class Starship(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)

class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)