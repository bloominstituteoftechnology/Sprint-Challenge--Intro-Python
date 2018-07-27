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

# ---------------VEHICLE---------------
# Base Class = Vehicle
class Vehicle: 
    pass

# Subclass to Vehicle above
class GroundVehicle(Vehicle): 
    pass

# Subclass to GroundVehicle above
class Car(GroundVehicle): 
    pass

# Subclass to GroundVehicle above
class Motorcycle(GroundVehicle):
    pass

# ---------------AIRPLANE---------------

# Base Class = FlightVehicle
class FlightVehicle: 
    pass

# Subclass to FlightVehicle above
class Airplane(FlightVehicle): 
    pass

# Subclass to Vehicle left
class FlightVehicle(Vehicle): 
    pass

# ---------------SPACE SHIPS---------------

# Base Class = Starship
class Starship: 
    pass

# Subclass to FlightVehicle left
class Starship(FlightVehicle):
  pass
