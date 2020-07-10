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

# Base class:
class Vehicle():
    """
    Representation of a generic vehicle object.
    """
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    """
    Representation of a specialized type of Vehicle object that only operates 
    on the ground.
    """
    def __init__(self):
        super().__init__()
        pass

class Car(GroundVehicle):
    """
    Representation of a specialized type of GroundVehicle object that carries 
    passengers (usually on roads) and has 4 wheels.
    """
    def __init__(self):
        super().__init__()
        pass

class Motorcycle(GroundVehicle):
    """
    Representation of a specialized type of GroundVehicle object that carries 
    passengers and has 2 wheels.
    """
    def __init__(self):
        super().__init__()
        pass

class FlightVehicle(Vehicle):
    """
    Representation of a specialized type of Vehicle object that flies.
    """
    def __init__(self):
        super().__init__()
        pass

class Airplane(FlightVehicle):
    """
    Representation of a specialized type of FlightVehicle object that carries 
    passengers or cargo.
    """
    def __init__(self):
        super().__init__()
        pass

class Starship(FlightVehicle):
    """
    Representation of a specialized type of FlightVehicle object that goes to space! 
    (and/or is being built by SpaceX and might go to Mars...)
    """
    def __init__(self):
        super().__init__()
        pass
