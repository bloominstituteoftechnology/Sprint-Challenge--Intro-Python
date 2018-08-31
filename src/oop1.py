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

class Vehicle: #base class here
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name}"
    def __str__(self):
        return f"{self.name}"


class GroundVehicle(Vehicle):
    def __init__(self, name, description, tires):
        Vehicle.__init__(self, name, description)
    pass

class Car(GroundVehicle):
    pass

class FlightVehicle(Vehicle):
    pass
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass        