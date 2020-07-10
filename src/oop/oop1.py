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
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        print(f"{self.name}")
    pass

# Parent / Child
class GroundVehicle(Vehicle):
    pass

# Children
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle): 
    pass

# Base Class
class FlightVehicle(Vehicle):
    pass

# Children
class Airplane(FlightVehicle):
    pass
