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

# This is the base class for all vehicle
class Vehicle:
    pass


# This is a child class of Vehicle
class GroundVehicle(Vehicle):
    pass


# This is a child class of GroundVehicle
class Car(GroundVehicle):
    pass


# This is a child class of GroundVehicle
class Motorocycle(GroundVehicle):
    pass


# Flying Types
# This is the base base for flying vehicle and is a child class of Vehicle
class FightVehicle(Vehicle):
    pass


# This is a child class of FightVehicle
class Starship(FightVehicle):
    pass


# This is a child class of FightVehicle
class Airplane(FightVehicle):
    pass
