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

# Base Class
class Vehicle:
    def _init_(self, name):
        self.name = name

# Sub Classes

class GroundVehicle(Vehicle):
    def _init_(self, name):
        Vehicle._init_(self, name)

class Car(GroundVehicle):
    def _init_(self, name):
        GroundVehicle._init_(self, name)

class Motorcycle(GroundVehicle):
    def _init_(self, name):
        GroundVehicle._init_(self, name)

# Base Class = Vehicle
#Sub Classes
class FlightVehicle(Vehicle):
    def _init_(self, name):
        Vehicle._init_(self, name)

class Airplane(FlightVehicle):
    def _init_(self, name):
        FlightVehicle._init_(self, name)

class Starship(FlightVehicle):
    def _init_(self, name):
        FlightVehicle._init_(self, name)