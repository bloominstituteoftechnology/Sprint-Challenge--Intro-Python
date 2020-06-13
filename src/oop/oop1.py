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

# inheriting methods from Vehicle


class FlightVehicle(Vehicle):
    pass

# inheriting methods from Vehicle


class GroundVehicle(Vehicle):
    pass

# inheriting methods from FlightVehicle which inherit from Vehicle


class Starship(FlightVehicle):
    pass

# inheriting methods from FlightVehicle which inherit from Vehicle


class Airplane(FlightVehicle):
    pass

# inheriting methods from GroundVehicle which inherit from Vehicle


class Car(GroundVehicle):
    pass

# inheriting methods from GroundVehicle which inherit from Vehicle


class Motorcycle(GroundVehicle):
    pass
