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

class Vehicle: # base class
    pass

class FlightVehicle(Vehicle): # base -> gen 1
    pass

class GroundVehicle(Vehicle): # base -> gen 1
    pass
  
class Car(GroundVehicle): # gen 1 -> gen 2
    pass

class Motorcycle(GroundVehicle): # gen 1 -> gen 2
    pass

class Airplane(FlightVehicle): # gen 1 -> gen 2
    pass

class Starship(FlightVehicle): # gen 1 -> gen 2
    pass