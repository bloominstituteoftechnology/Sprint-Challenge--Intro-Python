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

class Vehicle:  #base class
    pass

## inherits from vechicle class
class GroundVehicle(Vehicle):
    pass
    
class FlightVehicle(Vehicle):
    pass

## inherits from ground vehicle class
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

##inherits from Flight Vehicle Class
class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass