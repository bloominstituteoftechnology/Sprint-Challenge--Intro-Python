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
    pass

class GroundVehicle(Vehicle): #base Vehicle
    # def __init__ ...
        # Vehicle__init__()
    pass

class FlightVehicle: #base Vehicle
    # def __init__ ...
        # Vehicle__init__()
    pass

class Car(GroundVehicle): #base GroundVehicle
    # def __init__ ...
        # GroundVehicle__init__()
    pass

class Motorcycle(GroundVehicle): #base GroundVehicle
    # def __init__ ...
        # GroundVehicle__init__()
    pass

class Airplane(FlightVehicle): #base FlightVehicle
    # def __init__ ...
        # FlightVehicle__init__()
    pass

class Starship(FlightVehicle): #base FlightVehicle
    # def __init__ ...
        # FlightVehicle__init__()
    pass