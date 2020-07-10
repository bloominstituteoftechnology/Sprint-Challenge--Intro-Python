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

# base: Vehicle (self)
class Vehicle:
    pass

# base: Vehicle
class FlightVehicle(Vehicle):
    pass

# base: FlightVehicle
class Starship(FlightVehicle):
    pass

# base: Vehicle
class GroundVehicle(Vehicle):
    pass

# base: GroundVehicle
class Car(GroundVehicle):
    pass

# base: GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# base: FlightVehicle
class Airplane(FlightVehicle):
    pass


