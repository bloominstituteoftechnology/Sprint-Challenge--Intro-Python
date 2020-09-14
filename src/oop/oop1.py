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

class FlightVehicle(Vehicle):
    pass
    # Vehicle

class Starship(FlightVehicle):
    pass
    # FlightVehicle

class GroundVehicle(Vehicle):
    pass
    # Vehicle

class Airplane(FlightVehicle):
    pass
    # FlightVehicle

class Car(GroundVehicle):
    pass
    # GroundVehicle

class Motorcycle(GroundVehicle):
    pass
    # GroundVehicle