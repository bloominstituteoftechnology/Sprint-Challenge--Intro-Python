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

"""
Base class
"""
class Vehicle():
  def __init__(self, name, year, weight):
    self.name = name
    self.year = year
    self.year = weight

class FlightVehicle(Vehicle):
  def __init__(self, name, year, weight, wings):
    super().__init__(name, year, weight)
    self.wings = none

class Airplane(FlightVehicle):
  def __init__(self, name, year, weight, wings):
    super().__init__()

class Starship(FlightVehicle):
  def __init__(self, name, year, weight, wings):
    super().__init__()

class GroundVehicle(Vehicle):
  def __init__(self, name, year, weight, wheels):
    super().__init__(wheels)
    self.wheels = wheels


class Car(GroundVehicle):
  def __init__(self, name, year, weight, wheels):
    super().__init__()

class Motorcycle(GroundVehicle):
  def __init__(self, name, year, weight, wheels):
    super().__init__()

honda_speed_bike = ('Speed Bike', 1993, 50, 2)
star_explorer = ('Star Explorer', 1500, 1000, 6)

print(honda_speed_bike)
print(star_explorer)
