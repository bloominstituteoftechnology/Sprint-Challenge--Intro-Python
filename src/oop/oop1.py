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

# This the Base class
class Vehicle():
    def __init__(self):
        pass

# THis class "FlightVehicle" inherit attribute(s) from the base class "Vehicle" It can be refer to as sub-class or child  
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# THis class "Starship" inherit attribute(s) from the base class "FlightVehicle" It can be 
# refer to as grand of child  of Vehicle class
class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
# THis class "Airplane" inherit attribute(s) from the base class "FlightVehicle" It can be 
# refer to as grand of child  of Vehicle class
class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

 
# THis class "GroundVehicle" inherit attribute(s) from the base class "Vehicle" It can be refer to as sub-class or child  
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# THis class "Car" inherit attribute(s) from the base class "GroundVehicle" It can be 
# refer to as grand of child  of Vehicle class
class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass
# THis class "Motorcycle" inherit attribute(s) from the base class "GroundVehicle" It can be 
# refer to as grand of child  of Vehicle class
class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass