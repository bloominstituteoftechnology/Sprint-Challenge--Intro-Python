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
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Vehicle subclasses
class FlightVehicle(Vehicle):
    def __init__(self, name, description):
        Vehicle.__init__(self, name, description)
        pass

class GroundVehicle(Vehicle):
    def __init__(self, name, description):
        Vehicle.__init__(self, name, description)
        pass

# FlightVehicle subclasses
class Airplane(FlightVehicle):
    def __init__(self, name, description):
        FlightVehicle.__init__(self, name, description)
        pass

class Starship(FlightVehicle):
    def __init__(self, name, description):
        FlightVehicle.__init__(self, name, description)
        pass

# GroundVehicle subclasses
class Car(GroundVehicle):
    def __init__(self, name, description):
        GroundVehicle.__init__(self, name, description)
        pass

class Motorcycle(GroundVehicle):
    def __init__(self, name, description):
        GroundVehicle.__init__(self, name, description)
        pass
