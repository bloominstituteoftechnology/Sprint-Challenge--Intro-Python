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



class Vehicle: #This is the base class
    pass

class FlightVehicle(Vehicle): #Inherits from Vehicle
    pass

class GroundVehicle(Vehicle): #Inherits from Vehicle
    pass

class Starship(FlightVehicle): #Inherits from FlightVehicle
    pass

class Airplane(FlightVehicle): #Inherits from FlightVehicle
    pass

class Car(GroundVehicle): #Inherits from GroundVehicle
    pass

class Motorcycle(GroundVehicle): #Inherits from GroundVehicle
    pass
