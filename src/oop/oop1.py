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

# This is the Base Class
class Vehicle:
    name = ""
## End of Base Class



# Vehicle Subclasses
class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass
## End of Vehicle Subclasses



# FlightVehicle Subclasses
class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
## End of FlightVehicle Subclasses



# GroundVehicle Subclasses
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
## End of GroundVehicle Subclasses


