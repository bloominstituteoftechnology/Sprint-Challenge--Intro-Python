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


class Vehicle:
    # def __init_(self, name):
    #     self.name = name
    pass

# groundvehicles from vehicle
# t_type specifies travel type ex: ground, water, air, space


class GroundVehicle(Vehicle):
    # def __init__(self, name, t_type):
    #     super().__init__(self, name)
    pass

# car from ground vehicle


class Car(Vehicle):
    # def __init__(self, name, speed, t_type, make, model, engine, seats):
    #     super().__init__(self, name, speed, t_type)
    pass
# motorcycle from ground vehicle


class Motorcycle(Vehicle):
    # def __init__(self, name, speed, t_type, make, model, engine, seats, helmet):
    #     super().__init__(self, name, speed, t_type)
    pass
# flightvehile from vehicle


class FlightVehicle(Vehicle):
    # def __init__(self, name, t_type):
    #     super().__init__(self, name)
    pass
# airplane from flightvehicle


class Airplane(FlightVehicle):
    # def __init__(self, name, t_type, speed, make, model, engine, seats, wingspan):
    #     super().__init__(self, name, t_type)
    pass
# starship from flightvehicle


class Starship(FlightVehicle):
    # def __init__(self, name, t_type, speed,  make, model, power_drive, occupancy):
    #     super().__init__(self, name, t_type)
    pass
