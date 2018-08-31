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
    def __init__(self, name=None, description=None, num_wheels=None):
        self.name = name
        self.description = description
        self.num_wheels = num_wheels

# Vehicle subclasses
class FlightVehicle(Vehicle):
    def __init__(self, name=None, description=None, num_wheels=None):
        Vehicle.__init__(self, name, description, num_wheels)

class GroundVehicle(Vehicle):
    def __init__(self, name=None, description=None, num_wheels=None):
        Vehicle.__init__(self, name, description, num_wheels)


# FlightVehicle subclasses
class Airplane(FlightVehicle):
    def __init__(self, name=None, description=None, num_wheels=None):
        FlightVehicle.__init__(self, name, description, num_wheels)

class Starship(FlightVehicle):
    def __init__(self, name=None, description=None, num_wheels=None):
        FlightVehicle.__init__(self, name, description, num_wheels)

# GroundVehicle subclasses
class Car(GroundVehicle):
    def __init__(self, name=None, description=None, num_wheels=None):
        GroundVehicle.__init__(self, name, description, num_wheels)

class Motorcycle(GroundVehicle):
    def __init__(self, name=None, description=None, num_wheels=None):
        GroundVehicle.__init__(self, name, description, num_wheels)
