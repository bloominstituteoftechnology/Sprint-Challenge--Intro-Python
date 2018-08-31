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

#Base class

class Vehicle():
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

#Check to see if hierarchies are set up correctly:
print(issubclass(FlightVehicle, Vehicle))
print(issubclass(Starship, FlightVehicle))
print(issubclass(Starship, Vehicle))
print(issubclass(Airplane, FlightVehicle))
print(issubclass(Airplane, Vehicle))
print(issubclass(GroundVehicle, Vehicle))
print(issubclass(Car, Vehicle))