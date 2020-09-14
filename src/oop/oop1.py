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
class Vehicle:  # Class for all Vehicle
    pass  # Base Class


class GroundVehicle(Vehicle):  # Class for GroundVehicles
    pass


class Motorcycle(GroundVehicle):
    pass


class FlightVehicle(Vehicle):  # Class for FlightVehicles
    pass  # Body Class


class Starship(FlightVehicle):  # Class for Space Vehicles
    pass
