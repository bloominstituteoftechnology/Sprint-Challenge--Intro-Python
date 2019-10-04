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

class GroundVehicle(Vehicle): # chile of vehicle, down to earth
    pass

class Car(GroundVehicle): # grandchild? Is that what youd call these?
    pass
class Motorcycle(GroundVehicle): 
    pass

class FlightVehicle(Vehicle): # chile of vehicle, head in the clouds
    pass

class Airplane(FlightVehicle): # grandkid jefferson
    pass

class Starship(FlightVehicle): # jefferson after college
    pass
