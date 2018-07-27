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

#this is the base class
class Vehicle:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def getName(self):
        return self.name

    def getSType(self):
        return self.type

    def __str__(self):
        return "%s is a %s" % (self.name, self.type)

class FlightVehicle(Vehicle):
    
    def __init__(self):
        super().__init__("flight")
