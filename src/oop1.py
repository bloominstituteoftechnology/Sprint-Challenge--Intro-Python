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

# Base Class
class Vehicle:
    def __init__(self, vehicle_type, make, model):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model

class FlightVehicle(Vehicle):
    def __init__(self, vehicle_type, make, model):
        super().__init__(vehicle_type, make, model)
        pass

class Starship(FlightVehicle):
    def __init__(self, vehicle_type, make, model):
        super().__init__(vehicle_type, make, model)
        pass

class Airplane(FlightVehicle):
    def __init__(self, vehicle_type, make, model):
        super().__init__(vehicle_type, make, model)
        pass

class GroundVehicle(Vehicle):
    def __init__(self, vehicle_type, make, model):
        super().__init__(vehicle_type, make, model)
        pass

class Motorcycle(GroundVehicle):
    def __init__(self, vehicle_type, make, model):
        super().__init__(vehicle_type, make, model)
        pass