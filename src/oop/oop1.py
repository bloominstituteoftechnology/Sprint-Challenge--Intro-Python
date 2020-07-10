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

# Base Class
class Vehicle:
    def __init__(self, stat=None):
        self.stat = stat


class GroundVehicle(Vehicle):
    def __init__(self, stat=None, ground=None):
        self.ground
        super().__init__(stat)


class Car(GroundVehicle, Vehicle):
    def __init__(self, stat=None, ground=None, car=None):
        self.car = car
        super().__init__(stat, ground, car)


class Motorcycle(GroundVehicle, Vehicle):
    def __init__(self, stat=None, ground=None, motorcycle=None):
        self.motorcycle = motorcycle
        super().__init__(stat, ground, motorcycle)


class FlightVehicle(Vehicle):
    def __init__(self, stat=None, flight=None):
        self.flight
        super().__init__(stat)


class Airplane(FlightVehicle, Vehicle):
    def __init__(self, stat=None, flight=None, plane=None):
        self.plane = plane
        super().__init__(stat, flight, plane)


class Starship(FlightVehicle, Vehicle):
    def __init__(self, stat=None, flight=None, ship=None):
        self.ship = ship
        super().__init__(stat, flight, ship)