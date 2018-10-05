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

class Vehicle:          #Base Class
    def __init__(self):
        self.description = 'I am a basic vehicle'
        pass

class FlightVehicle(Vehicle):   # One level deep
    def __init__(self):
        Vehicle.__init__(self)
        self.description = 'I am a flying vehicle'
        pass

class Starship(FlightVehicle):  #Two levels deep
    def __init__(self):
        FlightVehicle.__init__(self)
        self.description = 'I am a starship, your argument is invalid'
        pass

class GroundVehicle(Vehicle):   #One level deep
    def __init__(self):
        Vehicle.__init__(self)
        pass

class Airplane(FlightVehicle):  #Two levels deep
    def __init__(self):
        FlightVehicle.__init__(self)
        pass

class Car(GroundVehicle):   #Two levels deep
    def __init__(self):
        GroundVehicle.__init__(self)
        pass

class Motorcycle(GroundVehicle):    #Two levels deep
    def __init__(self):
        GroundVehicle.__init__(self)
        pass
