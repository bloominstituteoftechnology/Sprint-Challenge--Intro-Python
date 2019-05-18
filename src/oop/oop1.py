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

#BASE CLASS VEHICLE
class Vehicle:
    def __init__(self):
        self

class FlightVehicle(Vehicle):
    def __init__(self):
        self

class Starship(FlightVehicle):
    def __init__(self):
        self

class GroundVehicle(Vehicle):
    def __init__(self):
        self

class Car(GroundVehicle):
    def __init__(self):
        self

class Motorcycle(GroundVehicle):
    def __init__(self):
        self

class Airplane(FlightVehicle):
    def __init__(self):
        self