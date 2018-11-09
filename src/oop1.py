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
class Vehicle():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
        pass

class GroundVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        # Vehicle is the base class
        pass

class Car(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)
        # GroundVehicle is the base class
        pass


class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)
    # GroundVehicle is the base class
        pass


class FlightVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    # Vehicle is the base class
        pass

class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)
    # FlightVehicle is the base class
        pass

class Starship(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)
    # FlightVehicle is the base class
        pass

objects = [
    Vehicle(name="vehicle"),
    GroundVehicle(name="ground vehicle"),
    Car(name="car"),
    Motorcycle(name="motorcycle"),
    FlightVehicle(name="flight vehicle"),
    Airplane(name="airplane"),
    Starship(name="starship")
]

for object in objects:
    object.print_name()

