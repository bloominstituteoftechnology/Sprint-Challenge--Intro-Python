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


# Vehicle
class Vehicle:
    def __init__(self, maxPassengers, topSpeed, maxRange):
        self.maxPassengers = maxPassengers
        self.topSpeed = topSpeed
        self.maxRange = maxRange


class GroundVehicle(Vehicle):
    def __init__(self, runsGas, runsNuclear):
        self.runsGas = False
        self.runsNuclear = False


class Car(GroundVehicle):
    def __init__(self, doors, isConvertible):
        self.doors = doors
        self.isConvertible = False


class Motorcycle(GroundVehicle):
    def __init__(self, isSportbike, isCruiser, isDirtbike):
        self.isSportbike = False
        self.isCruiser = False
        self.isDirtbike = False


class FlightVehicle(Vehicle):
    def __init__(self, runsGas, runsNuclear):
        self.runsGas = False
        self.runsNuclear = False


class Starship(FlightVehicle):
    def __init__(self, doors, isConvertible):
        self.doors = doors
        self.isConvertible = False


class Airplane(FlightVehicle):
    def __init__(self, isSportbike, isCruiser, isDirtbike):
        self.isSportbike = False
        self.isCruiser = False
        self.isDirtbike = False
