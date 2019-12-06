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

# Vehicle class (Main base class)
class Vehicle(object):
    pass

# Base class is Vehicle
class FlightVehicle(Vehicle):
    pass

# Base class is FlightVehicle
class Starship(FlightVehicle):
    pass

# Base class is Vehicle
class GroundVehicle(Vehicle):
    pass

# Base class is GroundVehicle
class Car(GroundVehicle):
    pass

# Base Class is GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# Base class is FlightVehicle
class Airplane(FlightVehicle):
    pass