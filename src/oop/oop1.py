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


# Vehicle is the base class
class Vehicle():
    # Base class
    pass

# Flight vehicles, descended from Vehicle.


class FlightVehicle(Vehicle):
    # Base of this tree
    pass


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass

# Ground Vehicles, descended from Vehicle


class GroundVehicle(Vehicle):
    # Base of this tree
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass
