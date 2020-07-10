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

class Vehicle: #Base Class
    pass

class FlightVehicle(Vehicle): # is inheriting from Vehicle
    pass

class Starship(FlightVehicle): # is inheriting from Vehicle and FlightVehicle
    pass

class Airplane(FlightVehicle): # is inheriting from Vehicle and FlightVehicle
    pass

class GroundVehicle(Vehicle): # is inheriting from Vehicle
    pass

class Car(GroundVehicle): # is inheriting from Vehicle and GroundVehicle
    pass

class Motorcycle(GroundVehicle): # is inheriting from Vehicle and GroundVehicle
    pass