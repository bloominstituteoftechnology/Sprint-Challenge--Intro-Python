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

# base class
class Vehicle:
    pass

#Vehicle based
class FlightVehicle(Vehicle):
    pass

#FlightVehicle based
class Starship(FlightVehicle):
    pass

#Vehicle based
class GroundVehicle(Vehicle):
    pass

#FlightVehicle based
class Airplane(FlightVehicle):
    pass

#GroundVehicle based
class Car(GroundVehicle):
    pass

#Groundvehicle based
class Motorcycle(GroundVehicle):
    pass