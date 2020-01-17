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
#parent class
class Vehicle:
    pass

#child class of Vehicle
class GroundVehicle(Vehicle):
    pass

#child class of Vehicle
class FlightVehicle(Vehicle):
    pass

#sub type/base class of Ground Vehicle
class Car(GroundVehicle):
    pass

#sub type/base class of Ground Vehicle
class Motorcycle(GroundVehicle):
    pass

#sub type/base class of Flight Vehicle
class Airplain(FlightVehicle):
    pass

#sub type/base class of Flight Vehicle
class Starship(FlightVehicle):
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
