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
# vehicle

def Vehicle():
    pass


def GroundVehicle(Vehicle):
    pass


def Car(GroundVehicle):
    pass


def Motorcyle(GroundVehicle):
    pass

def FlightVehicle():
    pass

def Airplane(FlightVehicle):
    pass

def Starship():
    pass