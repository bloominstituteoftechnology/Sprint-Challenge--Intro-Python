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
    def __init__(self, name, type):
        self.name = name
        self.type = type

#child class
class GroundVehicle(Vehicle):
    def __init__(self, name, type):
        super.__init__(name, type)

#child class
class FlightVehicle(Vehicle):
    def __init__(self, name, type):
        super.__init__(name, type)