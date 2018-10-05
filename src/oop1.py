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

#BASE CLASS
class Vehicle:
    def __init__(self, name):
        self.name = name

class GroundVehicle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.name

class Car(GroundVehicle):
    def __init__(self, name):
        GroundVehicle.__init__(self, name)
        self.name

#BASE CLASS
class FlightVehicle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.name

class Airplane(FlightVehicle):
    def __init__(self, name):
        FlightVehicle.__init__(self, name)
        self.name

class Starship(FlightVehicle):
    def __init__(self, name):
        FlightVehicle.__init__(self, name)
        self.name