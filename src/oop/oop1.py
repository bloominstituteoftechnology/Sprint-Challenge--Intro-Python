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


## Vehicle class is the main Parent class
class Vehicle: 
    def __init__(self, vehicle, flight_vehicle, ship):
        self.vehicle = vehicle
        self.flight_vehicle = FlightVehicle(flight_vehicle)
        self.ship = ship
        
# Inhereted by Vehicle class, Parent of Starship Class
class FlightVehicle: 
    def __init__(self, starship):
        self.starship = Starship(starship) 

# Inhereted by FlightVehicle Class
class Starship:
    def __init__(self, starship):
        self.starship = starship
        

# Vehicle inherets all Sub classes below 
class GroundVehicle: 
    def __init__(self, car, motorcycle):
        self.car = Car(car)
        self.motorcycle = Motorcycle(motorcycle)
        
class Car: 
    def __init__(self, car):
        self.car = car
        
class Motorcycle: 
    def __init__(self, motorcycle):
        self.motor_cycle = motorcycle