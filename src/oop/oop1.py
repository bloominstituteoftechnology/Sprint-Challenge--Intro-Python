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
    pass
# Base class = Vehicle
class FlightVehicle(Vehicle):
    pass
# Base class = Flight Vehicle
class Starship(FlightVehicle):
    pass
# Base class = Vehicle
class GroundVehicle(Vehicle):
    pass
# Base class = Flight Vehicle
class Airplane(FlightVehicle):
    pass
# Base class = Ground Vehicle
class Car(GroundVehicle):
    pass
# Base class = Ground Vehicle
class Motorcycle(GroundVehicle):
    pass
