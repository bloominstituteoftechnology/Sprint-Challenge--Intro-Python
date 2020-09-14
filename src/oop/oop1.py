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

class Vehicle(): #BASE CLASS
    pass

class FlightVehicle(Vehicle): #type of vehicle
    pass

class Starship(FlightVehicle): #type of flight vehicle
    pass

class GroundVehicle(Vehicle): #inherits from vehicle
    pass

class Car(GroundVehicle): #inherits from ground vehicle
    pass

class Motorcycle(GroundVehicle): #inherits from ground vehicle
    pass

class Airplane(FlightVehicle): #inherits from flight vehicle
    pass

