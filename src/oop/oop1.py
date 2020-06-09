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
#BASE
class Vehicle:
    pass
#Child
class GroundVehicle(Vehicle):
    pass
#GrandChild
class Car(GroundVehicle):
    pass
#GrandChild
class Motorcycle(GroundVehicle):
    pass
#Child
class FlightVehicle(Vehicle):
    pass
#GrandChild
class Starship(FlightVehicle):
    pass
#GrandChild
class Airplane(FlightVehicle):
    pass