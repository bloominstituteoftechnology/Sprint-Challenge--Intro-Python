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

######
# Classes
#####

# Base Classes

class Vehicle:
  def __init__(self, name, description):
    pass

# Vehicle type classes

class FlightVehicle(Vehicle):
 def __init__(self, name, description, type):
  super().__init__(name, description)
  pass

class GroundVehicle(Vehicle):
  def __init__(self, name, description, type):
    super().__init__(name, description)
    pass

# Ground Vehicles

class Car(GroundVehicle):
  def __init__(self, name, description, type, make, model):
    super().__init__(name, description, type)
    pass

class Motorcycle(GroundVehicle):
  def __init__(self, name, description, type, make, model):
    super().__init__(name, description, type)
    pass

# Flight Vehicles

class Airplane(FlightVehicle):
  def __init__(self, name, description, type, make, model):
    super().__init__(name, description, type)
    pass

class Starship(FlightVehicle):
  def __init__(self, name, description, type, make, model):
    super().__init__(name, description, type)
    pass