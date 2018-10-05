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

# Vehicle is the base class
class Vehicle():
    def __init__(self, name, color):
        self.name = name
        self.color = color

class GroundVehicle(Vehicle):
    def __init__(self, name, color, numberOfTires):
        Vehicle.__init__(self, name, color)
        self.numberOfTires = numberOfTires

class Car(GroundVehicle):
    def __init__(self, name, color, numberOfTires, numberOfDoors):
        GroundVehicle.__init__(self, name, color, numberOfTires)
        self.numberOfDoors = numberOfDoors

class Motorcycle(GroundVehicle):
    def __init__(self, name, color, numberOfTires, numberOfDoors, typeOfMotorcycle):
        GroundVehicle.__init__(self, name, color, numberOfTires)
        self.typeOfMotorcycle = typeOfMotorcycle

class FlightVehicle(Vehicle):
    def __init__(self, name, color, propulsionSystem):
        Vehicle.__init__(self, name, color)
        self.propulsionSystem = propulsionSystem

class Airplane(FlightVehicle):
    def __init__(self, name, color, propulsionSystem):
        FlightVehicle.__init__(self, name, color, propulsionSystem)
    def __str__(self):
        return self.name

class Starship(FlightVehicle):
    def __init__(self, name, color, propulsionSystem):
        FlightVehicle.__init__(self, name, color, propulsionSystem)
