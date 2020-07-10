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

# base class
class Vehicle:
    def __init__(self, name, ground_vehicle, flight_vehicle)
    pass


class GroundVehicle:
    def __init__(self, name, car, motorcycle)
    pass


class FlightVehicle:
    def __init__(self, name, airplane, starship)
    pass


class Car:
    def __init__(self, name, airplane, starship)
    pass
