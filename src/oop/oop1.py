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


# GroundVehicle is derived from the base class Vehicle
class GroundVehicle(Vehicle):
    pass


# Car is derived from the class GroundVehicle, which is derived from the
# base class Vehicle
class Car(GroundVehicle):
    pass


# Motorcycle is derived from the class GroundVehicle, which is derived from
# the base class Vehicle
class Motorcycle(GroundVehicle):
    pass


# FlightVehicle is derived from the base class Vehicle
class FlightVehicle(Vehicle):
    pass


# Starship is derived from the class FlightVehicle, which is derived from the
# base class Vehicle
class Starship(FlightVehicle):
    pass


# Airplane is derived from the class FlightVehicle, which is derived from the
# base class Vehicle
class Airplane(FlightVehicle):
    pass
