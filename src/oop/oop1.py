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

# baseclass, all sub classes branch off from here
class Vehicle():
    def __init__(self):
        pass
# inherents from vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        pass
# inherents from vehicle
class Starship(Vehicle):
    def __init__(self):
        pass
# inherents from vehicle
class GroundVehicle(Vehicle):
    def __init__(self):
        pass
# inherents from flight vehicle
class Airplane(FlightVehicle):
    def __init__(self):
        pass
# inherents from ground vehicle
class Car(GroundVehicle):
    def __init__(self):
        pass
# inherents from ground vehicle
class Motorcycle(GroundVehicle):
    def __init__(self):
        pass