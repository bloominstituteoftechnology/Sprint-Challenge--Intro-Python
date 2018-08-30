# Write classes for the following class hierarchy:
class Vehicle:
  def __init__(self, travel):
    self.travel = travel

class GroundVehicle(Vehicle):
  def __init__(self, travel, wheels):
    Vehicle.__init__(self, travel)
    self.wheels = wheels

class FlightVehicle(Vehicle):
  def __init__(self, travel, wings):
    Vehicle.__init__(self, travel)
    self.wings = wings

class Car(GroundVehicle):
  def __init__(self, travel, wheels, doors):
    GroundVehicle.__init__(self, travel, wheels)
    self.doors = doors

class Motorcycle(GroundVehicle):
  def __init__(self, travel, wheels, handlebars):
    GroundVehicle.__init__(self, travel, wheels)
    self.handlebars = handlebars

class Starship(FlightVehicle):
  def __init__(self, travel, wings, warpspeed):
    FlightVehicle.__init__(self, travel, wings)
    self.warpspeed = warpspeed

class Airplane(FlightVehicle):
  def __init__(self, travel, wings, knots):
    FlightVehicle.__init__(self, travel, wings)
    self.knots = knots

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
