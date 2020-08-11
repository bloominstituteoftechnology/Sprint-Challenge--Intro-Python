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
#-----------------------------------------------------------

# Base class:
class Vehicle():
    pass
#-----------------------------------------------------------

# This section contains Vehicles that travel in the air:
class FlightVehicle(Vehicle):
    pass

# This is a member of the FlightVehicle group -
class Starship(FlightVehicle):
    pass

# This is a member of the FlightVehicle group -
class Airplane(FlightVehicle):
    pass
#-----------------------------------------------------------

# This section contains Vehicles that travel on the ground:
class GroundVehicle(Vehicle):
    pass

# This is a member of the GroundVehicle group -
class Car(GroundVehicle):
    pass

# This is a member of the GroundVehicle group -
class Motorcycle(GroundVehicle):
    pass