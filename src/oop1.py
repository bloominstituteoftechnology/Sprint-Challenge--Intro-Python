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

class Vehicle: #Base Class for both ground and air type vehicles
    pass

# Ground type vehicles

class GroundVehicle(Vehicle): # Child class of vehicle base class
    pass

class Car(GroundVehicle): # Child class of groundvehicle class
    pass

class Motorocycle(GroundVehicle): # Child class of groundvehicle class
    pass


# Air type vehicles

class FightVehicle(Vehicle): # Child class of vehicle base class
    pass

class Starship(FightVehicle): # Child class of flightvehicle class
    pass

class Airplane(FightVehicle): # Child class of flightvehicle class
    pass