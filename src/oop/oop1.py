# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
class Vehicle: 
  # Vehicle is base class
  pass

# Inheriting methods from Vehicle

class FlightVehicle(Vehicle):
  pass

class GroundVehicle(Vehicle):
  pass

# Inheriting methods from FlightVehicle => Vehicle
class Starship(FlightVehicle):
  pass

class Airplane(FlightVehicle):
  pass

# Inheriting methods from GroundVehicle => Vehicle

class Car(GroundVehicle):
  pass

class Motorcycle(GroundVehicle):
  pass


  
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
