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
    # The base class
    pass

class FlightVehicle(Vehicle):
    # Inherits the class Vehicle
    pass

class Starship(FlightVehicle):
    # Inherits the class FlightVehicle
    pass

class Airplane(FlightVehicle):
    # Inherits the class FlightVehicle
    pass

class GroundVehicle(Vehicle):
    # Inherits the class Vehicle
    pass

class Car(GroundVehicle):
    # Inherits the class GroundVehicle
    pass

class Motorcycle(GroundVehicle):
    # Inherits the class GroundVehicle
    pass