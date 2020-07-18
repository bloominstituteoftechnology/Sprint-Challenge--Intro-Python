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
    # base class 
    pass 

class FlightVehicle(Vehicle): 
    # partially a base class? 
    pass  

class Starship(FlightVehicle): 
    # child class 
    pass 

class Airplane(FlightVehicle): 
    # child class 
    pass 

class GroundVehicle(Vehicle): 
    # partially a base class? 
    pass  

class Car(GroundVehicle): 
    # child class 
    pass 

class Motorcycle(GroundVehicle):
    # child class 
    pass 
