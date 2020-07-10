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

# base class - has 2 sub-classes: GroundVehicle, FlightVehicle
class Vehicle(): 
    pass

class GroundVehicle(Vehicle):
    #has 2 sub-classes: Car, Motorcycle
    pass

class FlightVehicle(Vehicle):
    #has 2 sub-classes: Airplane,Starship
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass