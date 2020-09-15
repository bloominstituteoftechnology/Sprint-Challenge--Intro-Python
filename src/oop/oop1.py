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
        self.data = []
        #Base Class

class GroundVehicle(Vehicle):
    def __init__(self):
        self.data = []

class Car(GroundVehicle, Vehicle):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Motorcycle(GroundVehicle, Vehicle):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class FlightVehicle(Vehicle):
    def __init__(self):
        self.data = []
class Airplane(FlightVehicle):
    def __init__(self):
        self.data = []

class Starship(FlightVehicle, Vehicle):
    def __init__(self):
        self.data = []
