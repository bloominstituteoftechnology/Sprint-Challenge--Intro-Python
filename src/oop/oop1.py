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
    def __init__(self):
        pass
    # base class for ALL vehicles

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass
    # Subclass from Vehicle, base class for all ground based vehicles

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass
    #Subclass from GroundVehicle (which subclasses from Vehicle).

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass
    #Subclass from GroundVehicle (which subclasses from Vehicle).

class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass
    # Subclass from Vehicle, base class for all flight based vehicles

class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
    # Subclass from FlightVehicle.

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
    # Subclass from FlightVehicle.
