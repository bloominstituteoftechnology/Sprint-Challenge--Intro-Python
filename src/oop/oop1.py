from abc import ABC

# This is base class
class Vehicle(ABC):
    pass

# GroundVehicle inherits from Vehicle
class GroundVehicle(Vehicle):
    pass

# Car inherits from GroundVehicle
class Car(GroundVehicle):
    pass

# Motorcycle inherits from GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# FlightVehicle inherits from Vehicle
class FlightVehicle(Vehicle):
    pass

# Starship inherits from FlightVehicle
class Starship(FlightVehicle):
    pass

# Airplane inherits from FlightVehicle
class Airplane(FlightVehicle):
    pass
