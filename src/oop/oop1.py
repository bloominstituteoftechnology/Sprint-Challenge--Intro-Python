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
#parent class
class Vehicle:
    pass

#child class
class GroundVehicle(Vehicle):
    pass

#sub type/base class
class Car(GroundVehicle):
    pass

#sub type/base class
class Motorcycle(GroundVehicle):
    pass

#child class 
class FlightVehicle(Vehicle):
    pass

#sub type/base class
class Airplane(FlightVehicle):
    pass

#sub type/base class
class Starship(FlightVehicle):
    pass