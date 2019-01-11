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

class Vehicle:
    pass
    # def __init__(self, wheels, windows):
    #     self.wheels = wheels
    #     self.windows = windows

class FlightVehicle(Vehicle):
    pass
    # def __init__(self, wheels, windows, flightHeight):
    #     super.__init__(wheels,windows)
    #     self.flightHeight = flightHeight

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass

class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass