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
    # This is going to be our base class for all vehicle classes.
    pass


class GroundVehicle(Vehicle):
    # Parent class for all ground vehicles (cars / motorcycles)
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


class FlightVehicle(Vehicle):
    # Parent class for all flying behicles (airplanes / starships)
    pass


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
