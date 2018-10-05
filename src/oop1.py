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


class Vehicle:    #base class is Vehicle
    pass

class GroundVehicle(Vehicle): #inherits Vehicle class
    pass

class Car(GroundVehicle): #inherits GroundVehicle class
    pass

class Motorcycle(GroundVehicle): #inherits GroundVehicle class
    pass

class FlightVehicle(Vehicle): #inherits Vehicle class
    pass

class Airplane(FlightVehicle): #inherits FlightVehicle class
    pass

class Starship(FlightVehicle): #inherits FlightVehicle class
    pass    
