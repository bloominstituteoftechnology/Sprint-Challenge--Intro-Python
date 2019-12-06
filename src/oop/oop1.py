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

# [x] 1 Parent --> Vehicle
# [x] 2 Children --> GroundVehicle &  FlightVehicle
# [x] 4 Grandchildren --> Car, Motorcycle, Airplane, Starship

class Vehicle:   #Base Class
    pass


# Group A
class GroundVehicle(Vehicle):   # Child 1;  #inherits from vehicle
    pass

class Car(GroundVehicle):    # Grandchild 1; inherits from GroundVehicle
    pass

class Motorcycle(GroundVehicle):    # Grandchild 2; inherits from GroundVehicle
    pass


# Group B
class FlightVehicle(Vehicle):   # Child 2; inherits from Vehicle
    pass

class Airplane(FlightVehicle):    # Grandchild 1;inherits from FlightVehicle 
    pass

class Starship(FlightVehicle):    # Grandchild 2; inherits from FlightVehicle
    pass
