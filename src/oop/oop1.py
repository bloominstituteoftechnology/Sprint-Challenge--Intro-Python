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
    #No base
class FlightVehicle(Vehicle):
    pass
    #Vehicle Base
class Starship(FlightVehicle):
    pass
    #FlightVehicle Base
class Airplane(FlightVehicle):
    pass
    #FlightVehicle Base
class GroundVehicle(Vehicle):
    pass
    #Vehicle Base
class Car(GroundVehicle):
    pass
    #GroundVehicle Base
class Motorcycle(GroundVehicle):
    pass
    #GroundVehicle Base    