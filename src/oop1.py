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


# Vehicle is the base class
class GroundVehicle(Vehicle):
    pass


# Vehicle is the base class
class Car(GroundVehicle):
    pass


# Vehicle is the base class
class Motorcycle(GroundVehicle):
    pass


# Vehicle is the base class
class FlightVehicle(Vehicle):
    pass


# Vehicle is the base class
class Airplane(FlightVehicle):
    pass


# Vehicle is the base class
class Starship(FlightVehicle):
    pass
