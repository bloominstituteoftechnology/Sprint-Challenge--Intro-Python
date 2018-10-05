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

# Highest level class (base class)
# 1
class Vehicle: 
    def __init__(self, engines):
        self.engines = engines

# Secondary class
# 1.1
class FlightVehicle(Vehicle):
    def __init__(self, engines, on_ground):
        Vehicle.__init__(self, engines)
        self.on_ground = False

# Third-level class 
# 1.1.1
class Starship(FlightVehicle):
    def __init__(self, engines, on_ground, in_earth):
        FlightVehicle.__init__(self, engines, on_ground)
        self.in_earth = False

# Third-level class
# 1.1.2
class Airplane(FlightVehicle):
    def __init__(self, engines, on_ground, in_earth):
        FlightVehicle.__init__(self, engines, on_ground)
        self.in_earth = True

# Secondary class
# 1.2
class GroundVehicle(Vehicle):
    def __init__(self, engines, on_ground):
        Vehicle.__init__(self, engines)
        self.on_ground = True

# Third-level class 
# 1.2.1
class Car(GroundVehicle):
    def __init__(self, engines, on_ground, in_earth, number_wheels):
        GroundVehicle.__init__(self, engines, on_ground)
        self.in_earth = True
        self.number_wheels = 4

# Third-level class
# 1.2.2
class Motorcycle(GroundVehicle):
    def __init__(self, engines, on_ground, in_earth):
        GroundVehicle.__init__(self, engines, on_ground)
        self.in_earth = True
        self.number_wheels = 2