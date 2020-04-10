"""
Write classes for the following class hierarchy:
 [Vehicle] ->  [FlightVehicle] -> [Starship]
     |                  \
     v                   v
[GroundVehicle]      [Airplane]
  |       |
  v       v
[Car]  [Motorcycle]
Each class can simply "pass" for its body. The exercise is about setting up
the hierarchy.
e.g.
class Whatever:
    pass
Put a comment noting which class is the base class
"""



class Vehicle:
    """base class for all vehicles"""
    
    pass
    
    
class Ground_Vehicle(Vehicle):
    """base class for all vehciles"""
    
    pass
    
class Car(Ground_Vehicle):
    """class represents all ground vehicles, inherts from base vehicle class"""
    
    pass
    
class Moped(Ground_Vehicle):

    pass
    

class Flight_Vehicle(Vehicle):

    pass
    
class Airplane(Flight_Vehicle):

    pass
    
class Starship(Flight_Vehicle):

    pass
    
    