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


# base class Vehicle
class Vehicle:
    def __init__(self):
        pass


# flying types


# subclass FlightVehicle is a child of Vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        pass


# subclass Starship is a child of FlightVehicle
class Starship(FlightVehicle):
    def __init__(self):
        FlightVehicle.__init__(self)
        pass


# subclass Airplane is a child of FlightVehicle
class Airplane(FlightVehicle):
    def __init__(self):
        FlightVehicle.__init__(self)
        pass


# ground types


# subclass GroundVehicle is a child of Vehicle
class GroundVehicle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        pass


# subclass Car is a child of GroundVehicle
class Car(GroundVehicle):
    def __init__(self):
        GroundVehicle.__init__(self)
        pass


# subclass Motorcycle is a child of GroundVehicle
class Motorcycle(GroundVehicle):
    def __init__(self):
        GroundVehicle.__init__(self)
        pass