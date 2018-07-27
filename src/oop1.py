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

# Vehicle class
class Vehicle:
  pass

# Ground Vehicle class
class GroundVehicle(Vehicle):
  pass

#Flight Vehicle class
class FlightVehicle(Vehicle):
  pass

# Car class
class Car(GroundVehicle):
  pass

# Motorcycle class
class Motorcycle(GroundVehicle):
  pass

# Airplane class
class Airplane(FlightVehicle):
  pass

# Starship class
class Starship(FlightVehicle):
  pass