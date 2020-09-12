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

class Vehicle(object):  # This is the base class
    pass


class FlightVehicle(Vehicle): # FlightVehicle is a type of Vehicle
    pass


class Starship(FlightVehicle): # Satarship is a type of FlightVehicle
    pass


class Airplane(FlightVehicle): # Airplane is a type of FlightVehicle
    pass


class GroundVehicle(Vehicle): # GroundVehicle is a type of Vehicle
    pass


class Car(GroundVehicle): # Car is a type of GroundVehicle
    pass


class Motorcycle(GroundVehicle): # Motorcylce is a type of GroundVehicle
    pass
