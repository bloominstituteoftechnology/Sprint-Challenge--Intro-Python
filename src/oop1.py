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
  def __init__(self, year, size):
    self.year = year
    self.size = size
  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__) + '\n \n'

class GroundVehicle(Vehicle):
  def __init__(self, year, size, name):
    super().__init__(year, size)
    self.name = name

class Car(GroundVehicle):
  def __init__(self, year, size, name, wheel_count):
    super().__init__(year, size , name)
    self.wheel_count = wheel_count

class Motorcycle(GroundVehicle):
  def __init__(self, year, size, name, wheel_count):
    super().__init__(year, size , name)
    self.wheel_count = wheel_count

class FlightVehicle(Vehicle):
  def __init__(self, year, size, name):
    super().__init__(year, size)
    self.name = name

class Airplane(FlightVehicle):
  def __init__(self, year, size, name, wing_size):
    super().__init__(year, size, name)
    self.wing_size = wing_size

class Starship(FlightVehicle):
  def __init__(self, year, size, name, reactor_type):
    super().__init__(year,size,name)
    self.reactor_type = reactor_type


v = Vehicle(1997, 'small')
g = GroundVehicle(1998, 'big', 'Mr. reliable')
c = Car(2000, 'medium', 'old blue', 4)
m = Motorcycle(1890, 'small', 'easy rider', 2)
f = FlightVehicle(2011, 'big', 'jet-fast')
a = Airplane(2014, 'big', 'big-plane', 'large wings')
s = Starship(3021, 'very big', 'enterprise', 'dark matter')

print(v,g,c,m,f,a,s)
