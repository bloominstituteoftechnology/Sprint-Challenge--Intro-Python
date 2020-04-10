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
    # base
    pass


class FlightVehicle(Vehicle):
    # 2nd level
    pass


class Starship(FlightVehicle):
    # 2nd level
    pass


class GroundVehicle(Vehicle):
    # 2nd level
    pass


class Airplane(FlightVehicle):
    # 2nd level
    pass


class Car(GroundVehicle):
    # 3rd
    pass


class Motorcycle(GroundVehicle):
    # 3rd
    pass
