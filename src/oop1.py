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
    def __init__(self, engine):
        self.engine = engine


class GroundVehicle(Vehicle):
    def __init__(self, engine, wheels):
        self.wheels = wheels
        super().__init__(engine)


class Car(GroundVehicle):
    def __init__(self, engine, wheels, make, model):
        self.model = model
        self.make = make
        super().__init__(engine, wheels)


class Motorcycle(GroundVehicle):
    def __init__(self, engine, wheels):
        super().__init__(engine, wheels)


class FlightVehicle(Vehicle):
    def __init__(self, engine, model):
        self.model = model
        super().__init__(engine)


class Airplane(FlightVehicle):
    def __init__(self, engine, model):
        super().__init__(engine, model)


class Starship(FlightVehicle):
    def __init__(self, engine, model):
        super().__init__(engine, model)
