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

#base class
class Vehicle:
    pass

#subclass of Vehicle
class FlightVehicle(Vehicle):
    pass

#subclasses of FlightVehicle:
class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

#subclass of Vehicle
class GroundVehicle(Vehicle):
    pass

#subclasses of GroundVehicle:
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass