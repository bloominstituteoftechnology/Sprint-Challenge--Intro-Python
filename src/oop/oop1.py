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
###################### * MY CODE * ############################

#base class
class Vehicle:
        pass

#subclasses of Vehicle

class GroundVehicle(Vehicle):
        pass

class FlightVehicle(Vehicle):
    pass

#subclasses for GroundVehicle

class Motorcycle(GroundVehicle):
    pass

class Car(GroundVehicle):
    pass

#subclasses for FlightVehicle

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass