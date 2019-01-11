# Write classes for the following class hierarchy:
class Vehicle:
    pass

class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass
    #Base Class : Vehicle

class Airplane(FlightVehicle):
    pass
    #Base Class : Vehicle

class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass
    #Base Class : Vehicle

class Motorcycle(GroundVehicle):
    pass
    #Base Class : Vehicle
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
