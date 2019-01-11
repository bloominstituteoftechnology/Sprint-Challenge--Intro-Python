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


# Vehicle

class Vehicle:
    pass


# Flight Vehicle

class FlightVehicle(Vehicle): 
    pass
    # Base Class: Vehicle

class Starship(FlightVehicle): 
    pass
    # Base Class: FlightVehicle

class Airplane(FlightVehicle): 
    pass
    # Base Class: FlightVehicle



# Ground Vehicle

class GroundVehicle(Vehicle): 
    pass
    # Base Class: Vehicle

class Car(GroundVehicle): 
    pass
    # Base Class: GroundVehicle
    
class Motorcycle(GroundVehicle): 
    pass
    # Base Class: GroundVehicle