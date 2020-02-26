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


class Vehicle(): #base
  pass

class GroundVehicle(Vehicle):
  pass

class Car(GroundVehicle):
  pass

class Motorcycle(GroundVehicle):
  pass
  
# ###########################

class FlightVehicle(Vehicle): 
  pass
#   def __init__(self,vehicle):
#     self.vehicle = vehicle

  
class Airplane(FlightVehicle):
  pass
#   def __init__(self,Vehicle):
#     self.vehicle = Vehicle

# # ####################
class Starship(FlightVehicle):
  pass
#   def __init__(self,vehicle):
#     self.vehicle = vehicle
#     print(vehicle)

# box = Vehicle('shape')

# shape = GroundVehicle('car')

# count = Type(4)

