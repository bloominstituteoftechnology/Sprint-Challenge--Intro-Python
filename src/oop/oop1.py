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

# Vehicle is the base class.
class Vehicle: 
    pass

# classes that are sublclassing from GroundVehicle
class GroundVehicle(Vehicle): 
     pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass


# Classes that are sublclassing from flight Vehicle
class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
