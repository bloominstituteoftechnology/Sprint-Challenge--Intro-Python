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
    def __init__(self):
        pass


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
    pass


class StarShip(FlightVehicle):
    def __init__(self):
        super().__init__()
    pass


class Airplane(FlightVehicle):
    def __init__(self):
        super.__init__()
    pass


class GroundVehicle(Vehicle):
    def __init__(self):
        super.__init__()
    pass


class Car(Vehicle):
    def __init__(self):
        super.__init__()
    pass


class MotorCycle(Vehicle):
    def __init__(self):
        super.__init__()
    pass
