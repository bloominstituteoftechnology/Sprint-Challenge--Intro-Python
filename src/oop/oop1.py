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

###Base Class
class Vehicle():
    pass

###FlightVehicle subclass of Vehicle
class FlightVehicle(Vehicle):
    pass

###Airplane class - subclass of FlightVehicle
class Airplane(FlightVehicle):
    pass

###Starship class - subclass of FlightVehicle
class Starship(FlightVehicle):
    pass

###GroundVehicle subclass of Vehicle
class GroundVehicle(Vehicle):
    pass

###Car class - subclass of Vehicle
class Car(GroundVehicle):
    pass

###Motorcycle class - subclass of Vehicle
class Motorcycle(GroundVehicle):
    pass