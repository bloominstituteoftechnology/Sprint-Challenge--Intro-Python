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

class Vehicle: #base class
    def __init__(self, *args, **kwargs):
        pass

class FlightVehicle(Vehicle):
    def __init__(self, *args, **kwargs):
        Vehicle.init(self, *args, **kwargs)
        pass

class Airplane(Vehicle, FlightVehicle):
    def __init__(self, *args, **kwargs):
        Vehicle.init(self, *args, **kwargs)
        FlightVehicle.init(self, *args, **kwargs)
        pass

class Starship(Vehicle, FlightVehicle):
    def __init__(self, *args, **kwargs):
        Vehicle.init(self, *args, **kwargs)
        FlightVehicle.init(self, *args, **kwargs)
        pass

class GroundVehicle(Vehicle):
    def __init__(self, *args, **kwargs):
        Vehicle.init(self, *args, **kwargs)
        pass

class Car(Vehicle, GroundVehicle):
    def __init__(self, *args, **kwargs):
        Vehicle.init(self, *args, **kwargs)
        GroundVehicle(self, *args, **kwargs)
        pass

class Motorcycle(Vehicle, GroundVehicle):
    def __init__(self, *args, **kwargs):
        Vehicle.init(self, *args, **kwargs)
        GroundVehicle(self, *args, **kwargs)
        pass
