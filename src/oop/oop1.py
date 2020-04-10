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


class Vehicle():
    pass


class FlightVehicle(Vehicle):  # vehicle
    pass


class Airplane(FlightVehicle):  # flightvehicle
    pass


class Starship(FlightVehicle):  # flightvehicle
    pass


class GroundVehicle(Vehicle):  # vehicle
    pass


class Car(GroundVehicle):  # groundVehicle
    pass


class Motorcycle(GroundVehicle):  # groundVehicle
    pass
