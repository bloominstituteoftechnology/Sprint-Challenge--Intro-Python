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


class Vehicle:  # base class
    def __init__(self, wheels=4):
        self.wheels = wheels


class FlightVehicle(Vehicle):
    def __init__(self, wheels=4, wings=2):
        super().__init__(wheels)
        self.wings = wings


class GroundVehicle(Vehicle):
    def __init__(self, wheels=4):
        super().__init__(wheels)


class Car(GroundVehicle):
    def __init__(self):
        super().__init__(4)


class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(2)


class Airplane(FlightVehicle):
    def __init__(self, wings=2):
        super().__init__(3, wings)


class Starship(FlightVehicle):
    def __init__(self):
        super().__init__(0, 2)
