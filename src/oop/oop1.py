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


# base class for all classes
class Vehicle:
    pass


# base class for all ground vehicles, child of Vehicle
class GroundVehicle(Vehicle):
    pass


# base class for all flight vehicles, child of Vehicle
class FlightVehicle(Vehicle):
    pass


#  child of flight vehicle
class Starship(FlightVehicle):
    pass

# child of flight vehicle
class Airplane(FlightVehicle):
    pass


# child of GroundVehicle
class Car(GroundVehicle):
    pass

# child of GroundVehicle
class Motorcycle(GroundVehicle):
    pass