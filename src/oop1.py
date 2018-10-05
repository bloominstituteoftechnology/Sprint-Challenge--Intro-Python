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

class Vehicle():
    pass

class FlightVehicle(Vehicle):
    # base class is Vehicle
    pass

class Starship(FlightVehicle):
    # base class is FlightVehicle
    pass

class Airplane(FlightVehicle):
    # base class is FlightVehicle
    pass

class GroundVehicle(Vehicle):
    # base class is Vehicle
    pass

class Car(GroundVehicle):
    # base class is GroundVehicle
    pass

class Motorcycle(GroundVehicle):
    # base class is GroundVehicle
    pass