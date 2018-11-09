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
# Put a comment noting which class is the base class

# BASE CLASS
class Vehicle: 
    def __init__(self, engines):
        self.engines = engines


# FlIGHT VEHICLES
class FlightVehicle(Vehicle):
    def __init__(self, engines, on_ground):
        Vehicle.__init__(self, engines)
        self.on_ground = False


class Starship(FlightVehicle):
    def __init__(self, engines, on_ground, in_earth):
        FlightVehicle.__init__(self, engines, on_ground)
        self.in_earth = False


class Airplane(FlightVehicle):
    def __init__(self, engines, on_ground, in_earth):
        FlightVehicle.__init__(self, engines, on_ground)
        self.in_earth = True


# GROUND VEHICLES
class GroundVehicle(Vehicle):
    def __init__(self, engines, on_ground):
        Vehicle.__init__(self, engines)
        self.on_ground = True


class Car(GroundVehicle):
    def __init__(self, engines, on_ground, in_earth, number_wheels):
        GroundVehicle.__init__(self, engines, on_ground)
        self.in_earth = True
        self.num_wheels = 4


class Motorcycle(GroundVehicle):
    def __init__(self, engines, on_ground, in_earth):
        GroundVehicle.__init__(self, engines, on_ground)
        self.in_earth = True
        self.num_wheels = 2