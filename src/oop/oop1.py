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

# Base class: Vehicle
class Vehicle:
    pass

# Class FlightVehicle is a type of Vehicle (child of Vehicle)
class FlightVehicle(Vehicle):
    pass

# Class Airplane is a type of FlightVehicle 
#   (child of FlightVehicle, grandchild of Vehicle)
class Airplane(FlightVehicle):
    pass

# Class Starship is a type of FlightVehicle 
#   (child of FlightVehicle, grandchild of Vehicle)
class Starship(FlightVehicle):
    pass

# GroundVehicle is a type of Vehicle
#   (child of Vehicle)
class GroundVehicle(Vehicle):
    pass

# Car is a type of GroundVehicle
#   (child of GroundVehicle; grandchild of Vehicle)
class Car(GroundVehicle):
    pass

# Motorcycle is a type of GroundVehicle
#   (child of GroundVehicle; grandchild of Vehicle)
class Motorcycle(GroundVehicle):
    pass
