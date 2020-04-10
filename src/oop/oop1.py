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

# Vehicle class, parent class
class Vehicle:
    pass

# This is the child class inherits from Vehicle class
class FlightVehicle(Vehicle):
    pass

# Another child class inherits from Vehicle class
class GroundVehicle(Vehicle):
    pass

# Child class inherits from GroundVehicle class
class Car(GroundVehicle):
    pass

# Child class inherits from GroundVehicle class
class Motorcycle(GroundVehicle):
    pass

# Child class inherits from FlightVehicle class
class Airplane(FlightVehicle):
    pass

# Child class inherits from FlightVehicle class
class Starship(FlightVehicle):
    pass
