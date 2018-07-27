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


class Vehicle:  # Base Class
    pass


class GroundVehicle(Vehicle):  # vehicle subclass
    pass


class Car(GroundVehicle):  # subclass of GroundVehicle, and Vehicle
    pass


class Motorcycle(GroundVehicle):  # subclass of GroundVehicle, and Vehicle
    pass


class FlightVehicle(Vehicle):  # subclass of Vehicle
    pass


class Airplane(FlightVehicle):  # subclass of FlightVehicle, and Vehicle
    pass


class Starship(FlightVehicle):  # subclass of FlightVehicle, and vehicle
    pass
