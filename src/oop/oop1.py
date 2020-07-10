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
class Vehicle:
    # each and every python class inherits from the base class object in python
    pass

class FlightVehicle(Vehicle):
    # FlightVehicles inherits from the Vehicle base class
    pass
class Starship(FlightVehicle):
    # FlightVehicles inherits from the FlightVehicle base class
    pass
class Airplane(FlightVehicle):
    # FlightVehicles inherits from the FlightVehicle base class
    pass

class GroundVehicle(Vehicle):
    # FlightVehicles inherits from the Vehicle base class
    pass
class Car(GroundVehicle):
    # FlightVehicles inherits from the GroundVehicle base class
    pass
class Motorcycle(GroundVehicle):
    # FlightVehicles inherits from the GroundVehicle base class
    pass