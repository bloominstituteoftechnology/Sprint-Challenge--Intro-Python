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


# Parent Class
class Vehicle:
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

# Inherits from Vehicle
class GroundVehicle(Vehicle):
    def __init__(self, name, engine, num_tires):
        super.__init__(name, engine)
        self.num_tires = num_tires

# Inherits from GroundVehicle
class Car(GroundVehicle):
    def __init__(self, name, engine, num_tires, num_doors):
        super.__init__(name, engine, num_tires)
        self.num_doors = num_doors

# Inherits from Vehicle
class FlightVehicle(Vehicle):
    def __init__(self, name, engine, num_engines):
        super.__init__(name, engine)
        self.num_engines = num_engines

class Airplane(FlightVehicle):
    def __init__(self, name, engine, num_engines, num_seats):
        super.__init__(name, engine, num_engines)
        self.num_seats = num_seats

class Starship(FlightVehicle):
    def __init__(self, name, engine, num_engines, num_blasters):
        super.__init__(name, engine, num_engines)
        self.num_blasters = num_blasters