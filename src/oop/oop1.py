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
#base class
class Vehicle: 
    def _init_(self):
     
       pass

class GroundVehicle(Vehicle):
    def _init_(self):
      super()._init_()
      pass

class Car(GroundVehicle):
    def _init_(self):
      super()._init_()
      pass

class Motorcycle(GroundVehicle):
    def _init_(self):
      super()._init_()
      pass

class FlightVehicle(Vehicle):
    def _init_(self):
      super()._init_()
      pass  

class Airplane(FlightVehicle):
    def _init_(self):
      super()._init_()
      pass

class Starship(FlightVehicle):
    def _init_(self):
      super()._init_()
      pass
