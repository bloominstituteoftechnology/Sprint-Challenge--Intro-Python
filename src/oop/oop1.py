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

class Vehicle():
    # Vehicle is the base class for GroundVehicle() and FlightVehicle()
    def __init__(self, engine, color, name):
        self.engine = engine
        self.color = color
        self.name = name

class GroundVehicle(Vehicle):
    # GroundVehicle is the base class for Motorcycle() and Car()
    pass

class Motorcycle(GroundVehicle):
    pass

class Car(GroundVehicle):
    pass

class FlightVehicle(Vehicle):
    # FlightVehicle() is the base class for Starship() and Airplane()
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
