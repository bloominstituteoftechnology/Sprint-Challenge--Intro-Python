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
    pass

# Base is Vehicle
class FlightVehicle(Vehicle):
    pass

# Base is FlightVehicle
class Starship(FlightVehicle):
    pass

# Base is Vehicle
class GroundVehicle(Vehicle):
    pass

# Base is FlightVehicle
class Airplane(FlightVehicle):
    pass

# Base is GroundVehicle
class Car(GroundVehicle):
    pass

# Base is GroundVehicle
class Motorcycle(GroundVehicle):
    pass

