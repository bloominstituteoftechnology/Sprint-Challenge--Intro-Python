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

#Base class
class Vehicle:
    """Vehicle creates a generic Vehicle object."""
    pass

class FlightVehicle(Vehicle):
    """FlightVehicle inherits from Vehicle"""
    def __init__(self):
        super(Vehicle, self).__init__()
        self.arg = arg
    pass

class Airplane(FlightVehicle):
    """Airplane inherits from FlightVehicle which inherits from Vehicle"""
    def __init__(self, arg):
        super(Airplane, self).__init__()
        self.arg = arg


class Starship(FlightVehicle):
    """Starship inherits from FlightVehicle class which inherits from Vehicle"""
    def __init__(self, arg):
        super(FlightVehicle, self).__init__()
        self.arg = arg

class GroundVehicle(Vehicle):
    """GroundVehicle inherits from Vehicle"""
    def __init__(self, arg):
        super(Vehicle, self).__init__()
        self.arg = arg

class Motorcycle(GroundVehicle):
    """Motorcycle inherits from GroundVehicle"""
    def __init__(self, arg):
        super(GroundVehicle, self).__init__()
        self.arg = arg

class Car(GroundVehicle):
    """Car inherits from GroundVehicle which inherits from Vehicle"""
    def __init__(self, arg):
        super(GroundVehicle, self).__init__()
        self.arg = arg
