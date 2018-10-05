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

class Vehicle: #base class
    def __init__(self, wheels, steering):
        self.wheels = wheels
        self.steering = steering

class FlightVehicle: # base class
    def __init__(self, engineType):
        self.engineType = engineType

class Starship: # base class
    def __init__(self, typeOf, speed):
        self.typeOf = typeOf
        self.speed = speed

class GroundVehicle(Vehicle): 
    def __init__(self, engine):
        self.engine = engine
        super().__init__(wheels, steering)

class Car(GroundVehicle):
    def __init__(self, brand, mpg):
        self.brand = brand
        self.mpg = mpg
        super().__init__(wheels, steering, engine)

class Motorcycle(GroundVehicle):
    def __init__(self, brand, mpg):
        self.brand = brand
        self.mpg = mpg
        super().__init__(wheels, steering, engine)

class Airplane(FlightVehicle):
    def __init__(self, capacity)
        self.capacity = capacity
        super().__init__(engineType)

