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

# Base Class
class Vehicle():
    def __init__(self):
        pass

# Flight Vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# Starship
class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# Airplane
class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# Ground Vehicle
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# Car
class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

# Motorcycle
class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass