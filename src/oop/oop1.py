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

class FlightVehicle(Vehicle):  # Baseclass is Vehicle
    pass

class Starship(FlightVehicle): # Baseclass is FlightVehicle
    pass

class GroundVehicle(Vehicle): # Baseclass is Vehicle
    pass

class Airplane(FlightVehicle): # Baseclass is FlightVehicle
    pass

class Car(GroundVehicle): # Baseclass is GroundVehicle
    pass

class Motorcycle(GroundVehicle): # Baseclass is GroundVehicle
    pass