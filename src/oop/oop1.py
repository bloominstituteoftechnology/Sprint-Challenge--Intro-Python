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

class Vehicle: # Base class
    # def __init__(self, name, color):
    #     self.name = name
    #     self.color = color
    pass

class GroundVehicle(Vehicle):
    # def__init__(self, name, color):
    #     super().__init__(name, color, wheels)
    #     self.name = name
    #     self.color = color
    #     self.wheels = wheels
    pass

class FlightVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass