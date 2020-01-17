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
    def __init__(self, vehicle, flight, ship):
        self.vehicle = vehicle
        self.flight = flight
        self.ship = ship
        
        
class FlightVehicle: 
    def __init__(self, airplane):
        self.airplane = airplane
        
class Starship:
    def __init__(self, starship):
        self.starship = starship