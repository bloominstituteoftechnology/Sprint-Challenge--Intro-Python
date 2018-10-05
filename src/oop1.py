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
#base class
    pass
class Flightvehicle(Vehicle):
    pass
class Starship(Flightvehicle):
    pass
class Airplane(Flightvehicle):
    pass
class Groundvehicle(Vehicle):
    pass
class Car(Groundvehicle):
    pass
class Motorcycle(Groundvehicle):
    pass