# Base class
class Vehicle:
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass