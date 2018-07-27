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


# BASE CLASS
class Vehicle:
  pass

#######################################

# SUBCLASS OF VEHICLE
class FlightVehicle(Vehicle):
  pass


# SUBCLASS OF FLIGHTVEHICLE
class Starship(FlightVehicle):
  pass


# SUBCLASS OF FLIGHTVEHICLE
class Airplane(FlightVehicle):
  pass

#######################################

# SUBCLASS OF VEHICLE
class GroundVehicle(Vehicle):
  pass


# SUBCLASS OF GROUNDVEHICLE
class Car(GroundVehicle):
  pass


# SUBCLASS OF GROUNDVEHICLE
class Motorcycle(GroundVehicle):
  pass
