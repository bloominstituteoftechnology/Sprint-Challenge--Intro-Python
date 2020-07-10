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

# Vehicle class
class Vehicle:
    pass


# Ground Vehicle
class GroundVehicle(Vehicle):
    pass


# car
class Car(GroundVehicle):
    pass


# Motorcycle
class Motorcycle(GroundVehicle):
    pass


# Flight Vehicle
class FlightVehicle(Vehicle):
    pass


# Airplane
class Airplane(FlightVehicle):
    pass


# Starship
class Starship(FlightVehicle):
    pass

