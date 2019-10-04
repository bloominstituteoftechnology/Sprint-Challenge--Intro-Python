# Write classes for the following class hierarchy:
class Vehicle:
    pass
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
class FlightVehicle(Vehicle):
    pass

class Starship (FlightVehicle):
    pass 
#[Airplane]
    
class Airplane (FlightVehicle):
    pass
# [GroundVehicle]  
    
class GroundVehicle(Vehicle):
    pass
#   |       |
#   v       v
# [Car]
class Car(GroundVehicle):
    pass
#  [Motorcycle]
    
class Motorcycle(GroundVehicle):
    pass
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
