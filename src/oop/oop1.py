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
    def__init__(self):
        pass
# Vehicle -> GroundVehicle
class GroundVehicle(Vehicle):
    def__init__(self):
        pass
# Vehicle -> GroundVehicle -> Car
class Car(GroundVehicle):
    def__init__(self):
        pass
# Vehicle -> GroundVehicle -> Motorcycle
class Motorcycle(GroundVehicle):
    def__init__(self):
        pass
# Vehicle -> FlightVehicle
class FlightVehicle:
    def__init__(self):
        pass
# Vehicle -> FlightVehicle -> Airplane
class Airplane(FlightVehicle):
    def__init__(self):
        pass
# Vehicle -> FlightVehicle -> Starship
class Starship(FlightVehicle):
    def__init__(self):
        pass
