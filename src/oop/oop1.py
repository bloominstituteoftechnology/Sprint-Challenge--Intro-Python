# Write classes for the following class hierarchy:

# No base class. It is the base class.
class Vehicle:
    pass

# Base class is Vehicle
class FlightVehicle(Vehicle):
    pass

# Base class  is FlightVehicle
class Starship(FlightVehicle):
    pass

# Base class is FlightVehicle
class Airplane(FlightVehicle):
    pass

# Base class is Vehicle
class GroundVehicle(Vehicle):
    pass

# Base class is GroundVehicle
class Car(GroundVehicle):
    pass

# Base class is GroundVehicle
class Motorcycle(GroundVehicle):
    pass


#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Put a comment noting which class is the base class
