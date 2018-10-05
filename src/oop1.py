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
class Vechicle():
    # baseclass
    pass
class FlightVehiclse(Vechicle):
    pass
class Airplane(FlightVechicle):
    pass
class Starship(FlightVechicle):
    pass

class GroundVechicle(Vechicle):
    pass

class Car(GroundVechicle):
    pass

class Motorcycle(GroundVechicle):