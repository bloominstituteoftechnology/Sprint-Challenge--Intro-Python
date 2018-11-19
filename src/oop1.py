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
    def __init__(self, name, description):
        self.name = name
        self.description = description

# base class for FlightVehicle and Starship


class FlightVehicle(Vehicle):
    pass
# takes in from Vehicle


class Starship(Vehicle):
    pass
# takes in from Vehicle


class GroundVehicle(Vehicle):
    pass
# base of Car and Motorcycle


class Car(GroundVehicle):
    pass
# takes in from GroundVehicle


class Motorcycle(GroundVehicle):
  pass
  #takes in from GroundVehicle

class Airplane(FlightVehicle):
  pass
  #takes in from FlightVehicle