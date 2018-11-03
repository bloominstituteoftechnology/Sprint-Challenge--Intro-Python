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

# Base Vehicle Class
class Vehicle():
    pass

# Sub Class of Vehicles
class GroundVehicle(Vehicle):
    pass

class FlightVehicle(Vehicle):
    pass

# Sub Class of Ground Vehicles
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# Sub Class Flight Vehicles
class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass