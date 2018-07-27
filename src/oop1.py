# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
class Vehicle:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        Vehicle is the base for the Ground and Flight Vehicles
class GroundVehicle(Vehicle):
    GroundVehicle is the base for Car and Motorcycle
    pass
class Car(GroundVehicle):
    pass
class Motorcycle(GroundVehicle):
    pass
class FlightVehicle(Vehicle):
    FlightVehicle is the base for Starship and Airplane
    pass
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass

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
