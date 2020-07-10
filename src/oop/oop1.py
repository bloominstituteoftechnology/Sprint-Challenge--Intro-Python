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

class Vehicle():
    """ The base class for vehicles """
    pass

class FlightVehicle(Vehicle):
    """ The base class for flying vehicles, inherits from Vehicle """
    pass

class Starship(FlightVehicle):
    """ The Starship class, inherits from FlightVehicle """
    pass

class Airplane(FlightVehicle):
    """ The Airplane class, inherits from FlightVehicle """
    pass

class GroundVehicle(Vehicle):
    """ The base class for ground vehicles, inherits from Vehicle """
    pass

class Car(GroundVehicle):
    """ The Car class, inherits from GroundVehicle """
    pass

class Motorcycle(GroundVehicle):
    """ The Motorcycle class, inherits from GroundVehicle """
    pass
