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
    #def __init__(self,name,category):
    #    self.name = name
    #    self.category = category
    pass

class GroundVehicle():
    #A groundVehicle is a Vehicle
    pass

class Car(GroundVehicle):
    #A car is a Groundvehicle, and a GroundVehicle is a Vehicle
    pass

class Motorcycle(GroundVehicle):
    #A Motorcycle is a Groundvehicle, and a GroundVehicle is a Vehicle
    pass

class FlightVehicle(Vehicle):
    #A FlightVehicle is a Vehicle
    pass

class Airplane(FlightVehicle):
    #An Airplane is a FlightVehicle, and a FlightVehicle is a Vehicle
    pass

class Starship(FlightVehicle):
    #A Starship is a Flightvehicle, and a FlightVehicle is a Vehicle
    pass

