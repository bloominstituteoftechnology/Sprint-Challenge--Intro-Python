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

# Base Class Vehicle
class Vehicle:
    pass

# Subclass of vehicle and Base Class for FlyingVehicle
class FlightVehicle(Vehicle):
    pass

# Subclass of vehicle and Base Class for GroundVehicle
class GroundVehicle(Vehicle):
    pass

# Subclass of FlightVehicle
class Starship(FlightVehicle):
    pass

# Subclass of FlightVehicle
class Airplane(FlightVehicle):
    pass

# Subclass of GroundVehicle
class Car(GroundVehicle):
    pass

# Subclass of GroundVehicle
class Motorcycle(GroundVehicle):
    pass