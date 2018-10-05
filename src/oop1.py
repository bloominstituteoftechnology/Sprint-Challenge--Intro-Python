# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]


# Parent/Base Super Class
class Vehicle():
    def __init__(self):
        pass


# Parent Class to inheriting FlightVehicle Classes
class FlightVehicle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        pass


class Starship(FlightVehicle):
    def __init__(self):
        FlightVehicle.__init__(self)
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        FlightVehicle.__init__(self)
        pass

#
# GroundVehicles
#
# Parent Class to inheriting GroundVehicle Classes


class GroundVehicle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        pass


class Car(GroundVehicle):
    def __init__(self):
        GroundVehicle.__init__(self)
        pass


class Motorcycle(GroundVehicle):
    def __init__(self):
        GroundVehicle.__init__(self)
        pass


# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
``
