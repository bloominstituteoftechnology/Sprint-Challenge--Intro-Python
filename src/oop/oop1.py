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

# Parent Class
class Vehicle():
    def __init__(self):
        pass



# Flight Vehicle Class
class FlightVehicle(Vehicle):
    pass

# Classes for both Flight Vehicles
class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass


# Ground Vehicle Class
class GroundVehicle(Vehicle):
    pass


# Classes for both Ground Vehicle
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass