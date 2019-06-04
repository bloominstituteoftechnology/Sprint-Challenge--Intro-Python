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

# Base class of all vehicle type objects
class Vehicle:
    def __init__(self):
        pass

# Base class FlightVehicle for flying vehicles. Inherits from Vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# Children of FlightVehicle
class Airplane(FlightVehicle):
    def __init__(self):
        pass

class Starship(FlightVehicle):
    def __init__(self):
        pass

# Base class GroundVehicle for ground vehicles. Inherits from Vehicle
class GroundVehicle(Vehicle):
    def __init__(self):
        pass

# Children of GroundVehicle
class Car(GroundVehicle):
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        pass
