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
  """Base class"""
  pass
   

class GroundVehicle(Vehicle):
  """Sub-class of Vehicle"""
  pass

class Car(GroundVehicle):
  """Sub-class of Groundvehicle"""
  pass

class Motorcycle(GroundVehicle):
  """Sub-class of Groundvehicle"""
  pass



class Flightvehicle(Vehicle):
  """Sub-class of Vehicle"""
  pass

class Startship(Flightvehicle):
  """Sub-class of Flightvehicle"""
  pass

class Airplane(Flightvehicle):
  """Sub-class of Flightvehicle"""
  pass