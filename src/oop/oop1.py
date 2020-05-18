"""
This file contains a sample class hierarchy for various vehicle types.
"""

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
    """
    This is the base class.
    """

class GroundVehicle(Vehicle):
    """
    This is a class for land vehicles.
    """

class FlightVehicle(Vehicle):
    """
    This is a class for airborne vehicles.
    """

class Car(GroundVehicle):
    """
    This a class for four-wheeled ground vehicles.
    """

class Motorcycle(GroundVehicle):
    """
    This is a class for two-wheeled ground vehicles.
    """

class Airplane(FlightVehicle):
    """
    This is a class for propeller and jet aircraft.
    """

class Starship(FlightVehicle):
    """
    This is a class for space vehicles.
    """
