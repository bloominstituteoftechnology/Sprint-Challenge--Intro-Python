# Write classes for the following class hierarchy:
#
#Parent of all classes
class Vehicle():
    def __init__(self, vehicle):
        self.vehicle = vehicle
        
# Base of Vehicle
class FlightVehicle(Vehicle):
    def __init__(self, vehicle, flight_vehicle):
        Vehicle.__init__(self, vehicle)
        self.flight_vehicle = flight_vehicle

#Base of FlightVehicle
class Starship(FlightVehicle):
    def __init__(self, vehicle, flight_vehicle, starship):
        FlightVehicle.__init__(self, vehicle, flight_vehicle)
        self.starship

#Base of Vehicle
class GroundVehicle(Vehicle):
    def __init__(self, vehicle, ground_vehicle):
        Vehicle.__init__(self, vehicle)
        self.ground_vehicle = ground_vehicle

#Base of FlightVehicle
class Airplane(FlightVehicle):
    def __init__(self, vehicle, flight_vehicle, airplane):
        FlightVehicle.__init__(self, vehicle, flight_vehicle)
        self.airplane = airplane

#Base of GroundVehicle
class Car(GroundVehicle):
    def __init__(self, vehicle, ground_vehicle, car):
        GroundVehicle.__init__(self, vehicle, ground_vehicle)
        self.car = car

#Base of GroundVehicle
class Motorcycle(GroundVehicle):
    def __init__(self, vehicle, ground_vehicle, motorcycle):
        GroundVehicle.__init__(self, vehicle, ground_vehicle)
        self.motorcycle = motorcycle
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
