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

# Base Class - All other classes are a form of vehicle
class Vehicle:
    pass

# child class of vehicle 
class FlightVehicle(Vehicle):
    pass

# child class of flight vehicle which is a child class of vehicle
class Starship(FlightVehicle):
    pass

# child class of flight vehicle which is a child class of vehicle
class Airplane(FlightVehicle):
    pass

# child class of Vehicle
class GroundVehicle(Vehicle):
    pass

# child class of Ground Vehicle
class Car(GroundVehicle):
    pass
    
# child class of Ground Vehicle
class Motorcycle(GroundVehicle):
    pass

