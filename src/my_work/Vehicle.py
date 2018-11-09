#Base Class
from  GroundVehicle import GroundVehicle

vehicles = {
    "red": GroundVehicle("red","4" ),
    "red": GroundVehicle("red","4"),
    "blue": Motorcycle("blue","2"),
    "red": GroundVehicle("red","4"),
    "blue": Motorcycle("blue","2"),
}

class Vehicle:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        