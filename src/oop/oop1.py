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

#base class
class Vehicle:
    """ This is a base class that represents a vehicle """
    def __init__(self):
        pass

# FlightVehicles

# Vehicle is base class
class FlightVehicle(Vehicle):
    """ This is a Flight Vehicle Class """
    def __init__(self, wingType: str = "Gilder"):
        super().__init__()
        self.wingType = wingType

# FlightVehicle is base class
class Starship(FlightVehicle):
    """ This is a Starship Vehicle Class """
    def __init__(self, wingType: str = "Piercer", trusterEngineType: str = "Hydrogen"):
        super().__init__(wingType=wingType)
        self.trusterEngineType = trusterEngineType

# FlightVehicle is base class
class Airplane(FlightVehicle):
    """ This is a Airplane Vehicle Class """
    def __init__(self, wingType: str = "Glider", jetEngineCount: int = 2):
        super().__init__(wingType=wingType)
        self.jetEngineCount = jetEngineCount


# Ground Vehicles

# Vehicle is base class
class GroundVehicle(Vehicle):
    """ This is a GroundVehicle Class """
    def __init__(self, wheelCount: int = 4):
        super().__init__()
        self.wheelCount = wheelCount


# GroundVehicle is base class
class Motorcycle(GroundVehicle):
    """ This is a Motorcycle Class """
    def __init__(self, wheelCount: int = 2, includesComplementaryLeatherJacket: bool = True):
        super().__init__(wheelCount=wheelCount)
        self.includesComplementaryLeatherJacket = includesComplementaryLeatherJacket


# GroundVehicle is base class
class Car(GroundVehicle):
    """ This is a Car Class """
    def __init__(self, wheelCount: int = 4, hasSunroof: bool = False):
        super().__init__(wheelCount=wheelCount)
        self.hasSunroof = hasSunroof

