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


#this is the base class
class Vehicle:
    pass


#inherits from Vehicle class
class FlightVehicle(Vehicle):
    pass


#inherits from FlightVehicle Class
class Airplane(FlightVehicle):
    pass


#inherits from FlightVehicle Class
class Starship(FlightVehicle):
    pass


#inherits from Vehicle Class
class GroundVehicle(Vehicle):
    pass


#inherits from Groundvehicle Class
class Car(GroundVehicle):
    pass


#inherits from Groundvehicle Class
class Motorcycle(GroundVehicle):
    pass
