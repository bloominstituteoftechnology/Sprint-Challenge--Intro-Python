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
    pass
#Base class: Vehicle
class Starship(FlightVehicle):
    pass
#Base class: FlightVehicle
class GroundVehicle(Vehicle):
    pass
#Base class: vehicle
class Motorcycle(GroundVehicle):
    pass
#Base class: GroundVehicle
class Car(GroundVehicle):
    pass
#Base class: GroundVehicle