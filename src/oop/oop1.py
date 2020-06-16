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

#Vehcile in base class
class Vehicle:
    pass

#Ground Vehicle inherits Vehicle
class GroundVehicle(Vehicle):
    pass

#Car inherits Ground Vehicle
class Motorcycle(GroundVehicle):
    pass

#Flight Vehicle inherits Vehicle
class FlightVehicle(Vehicle):
    pass

#Airplane inherits Flight Vehicle
class Airplane(FlightVehicle):
    pass

#Starship inherits FlightVehicle
class Starship(FlightVehicle):
    pass
