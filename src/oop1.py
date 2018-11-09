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

# everything starts as a Vehicle
class Vehicle:
    def __init__(self, num_wheels):
        pass
# flightvehicale is from vehicle
class FlightVehicle(Vehicle): 
    pass
# starship comes from flightvehicle
class Starship(FlightVehicle):
    pass
# airplane comes from flightvehicle
class Airplane(FlightVehicle):
    pass

# groundvehicle is from vehicle
class GroundVehicle(Vehicle):
    pass
# car is from groundvehicle
class car(GroundVehicle):
    pass
# motorcycle is from groundvehicle
class Motorcycle(GroundVehicle):
    pass
