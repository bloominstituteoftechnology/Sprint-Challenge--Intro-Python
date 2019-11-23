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


class Vehicle:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# base class is Vehicle
class FlightVehicle(Vehicle):
    def __init__(self, name, description, airtime):
        super().__init__(name, description)
        self.airtime = airtime

# base class is FlightVehicle


class Starship(FlightVehicle):
    def __init__(self, name, description, airtime, model):
        super().__init__(name, description, airtime)
        self.model = model

# base class is Vehicle


class GroundVehicle(Vehicle):
    def __init__(self, name, description, tires):
        super().__init__(name, description)
        self.tires = tires

# base class is GroundVehicle


class Car(GroundVehicle):
    def __init__(self, name, description, tires, model):
        super().__init__(name, description, tires)
        self.model = model

# base class is groundvehicle


class Motorcycle(GroundVehicle):
    def __init__(self, name, description, tires, cc):
        super().__init__(name, description, tires)
        self.cc = cc
