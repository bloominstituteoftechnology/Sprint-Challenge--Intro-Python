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

# Base class: Vehicle.


class Vehicle:
    pass


# Ground vehicles.
class GroundVehicle(Vehicle):
    pass


# Car, inherits from GroundVehicle.
class Car(GroundVehicle):
    pass


# Motorcycle, inherits from GroundVehicle.
class Motorcycle(GroundVehicle):
    pass


# Flight vehicles.
class FlightVehicle(Vehicle):
    pass


# Airplane, inherits from FlightVehicle.
class Airplane(FlightVehicle):
    pass


# Starship, inherits from FlightVehicle.
class Starship(FlightVehicle):
    pass
