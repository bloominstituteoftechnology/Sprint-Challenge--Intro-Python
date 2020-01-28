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

# Base class
class Vehicle:
    pass

# Subclass
class GroundVehicle(Vehicle):
    pass

# class of the Subclass
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# Base Class
class FlightVehicle(Vehicle):
    pass

#Subclass
class Airplane(FlightVehicle):
    pass

#Base Class
class Starship(FlightVehicle):
    pass
