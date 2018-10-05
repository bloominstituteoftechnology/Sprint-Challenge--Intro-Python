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
class Vehicle(object):
    def __init__(self, name, speed):
        self.name = name 
        self.speed = speed
    def __repr__(self):
        return """This is a base class """

class FlightVehicle(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self,name,speed)
    def __repr__(self):
        return """This is a subclass of Vehicle """
class Starship(Vehicle):
    def __init__(self,name,speed):
        Vehicle.__init__(self,name,speed)
    def __repr__(self):
        return """This is a subclass of Vehicle """