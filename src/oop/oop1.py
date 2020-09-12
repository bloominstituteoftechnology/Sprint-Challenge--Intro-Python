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


# Parent class
class Vehicle:
  pass

# Base class of Vehicle
class FlightVehicle(Vehicle):
  pass

# Base class of FlightVehicle
class Starship(FlightVehicle):
  pass

# Base class of Vehicle
class GroundVehicle(Vehicle):
  pass

# Base class of FlightVehicle
class Airplane(FlightVehicle):
  pass

# Base class of GroundVehicle
class Car(GroundVehicle):
  pass

# Base class of GroundVehicle
class Motorcycle(GroundVehicle):
  pass 

        
# OR EXAMPLE:

# # Parent class 
# class Vehicle:
#     def __init__(self, vehicle):
#         self.vehicle = vehicle

# # Base class of Vehicle
# class FlightVehicle(Vehicle):
#     def __init__(self, vehicle, flight_vehicle):
#         super().__init__(vehicle)
#         self.flight_vehicle = flight_vehicle

# # Base class of FlightVehicle
# class Starship(FlightVehicle):
#     def __init__(self, vehicle, flight_vehicle, starship):
#         super().__init__(vehicle, flight_vehicle)
#         self.starship = starship

# # Base class of Vehicle
# class GroundVehicle(Vehicle):
#     def __init__(self, vehicle, ground_vehicle):
#         super().__init__(vehicle)
#         self.ground_vehicle = ground_vehicle

# # Base class of FlightVehicle
# class Airplane(FlightVehicle):
#     def __init__(self, vehicle, flight_vehicle, airplane):
#         super().__init__(vehicle, flight_vehicle)
#         self.airplane = airplane

# # Base class of GroundVehicle
# class Car(GroundVehicle):
#     def __init__(self, vehicle, ground_vehicle, car):
#         super().__init__(vehicle, ground_vehicle)
#         self.car = car

# # Base class of GroundVehicle
# class Motorcycle(GroundVehicle):
#     def __init__(self, vehicle, ground_vehicle, motorcycle): 
#         super().__init__(vehicle, ground_vehicle)
#         self.motorcycle = motorcycle      

        
