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

# Base class: Definition for our base class Vehicle, which represents a generic 
# vehicle object:
class Vehicle():
    def __init__(self):
        pass

# Definition for class GroundVehicle, which represents a specialized type of Vehicle 
# object that only operates on the ground:
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# Definition for class Car, which represents a specialized type of GroundVehicle 
# object that carries passengers on roads (usually) and has 4 wheels:
class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

# Definition for class Motorcycle, which represents a specialized type of GroundVehicle 
# object that carries passengers and has 2 wheels:
class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

# Definition for class FlightVehicle, which represents a specialized type of Vehicle 
# object that flies;
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# Definition for class Airplane, which represents a specialized type of FlightVehicle 
# object that carries passengers or cargo:
class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# Definition for class Starship, which represents a specialized type of FlightVehicle 
# object that goes to space! (and/or one built by SpaceX that might go to Mars...):
class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
