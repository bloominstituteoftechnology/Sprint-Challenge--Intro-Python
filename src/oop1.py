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

# Vehicle (Base Class):
class Vehicle():
    def __init__(self, name):
        pass
        
# Ground        
class GroundVehicle(Vehicle): 
    def __init__(self, name):
        super().__init__(name)      
        pass

class Car(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)
        pass

class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)
        pass

#==========================================
# Air
#  
class FlightVehicle(Vehicle): 
    def __init__(self, name):
        super().__init__(name)      
        pass


class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)
        pass

class Starship(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)
        pass
