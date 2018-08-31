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

#   Land travel
class Vehicle: # Base class
  pass

class GroundVehicle(Vehicle): # subclass of vehicle
  pass

class Car(GroundVehicle):  # subclass of GroundVehicle
  pass

class Motorcycle(GroundVehicle):  # subclass of GroundVehicle
  pass


#   Air travel
class FlightVehicle(Vehicle): # subclass 
  pass

class Airplane(FlightVehicle): # subclass of FlightVehicle
  pass


#   Space travel
class Starship(FlightVehicle): # subclass of FlightVehicle
  pass