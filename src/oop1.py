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

class Vehicle: # base class
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.travelsRoads = False
        self.flies = False
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"

class FlightVehicle(Vehicle):
    def __init__(self, name, desc):
        Vehicle.__init__(self, name, desc)
        self.flies = True
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"

class Starship(FlightVehicle):
    def __init__(self, name, desc):
        Vehicle.__init__(self, name, desc)
        self.flyingAltitude = 'infinite'
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"

class Airplane(FlightVehicle):
    def __init__(self, name, desc):
        Vehicle.__init__(self, name, desc)
        self.flyingAltitude = 30,000
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"

class GroundVehicle(Vehicle):
    def __init__(self, name, desc):
        Vehicle.__init__(self, name, desc)
        self.travelsRoads = True
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"

class Car(GroundVehicle):
    def __init__(self, name, desc):
        GroundVehicle.__init__(self, name, desc)
        self.numWheels = 4
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"

class Motorcycle(GroundVehicle):
    def __init__(self, name, desc):
        GroundVehicle.__init__(self, name, desc)
        self.numWheels = 2
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"
    
    

