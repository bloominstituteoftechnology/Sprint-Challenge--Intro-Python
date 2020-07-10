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
class Vehicle: # Vehicle is the base class for all other classes

    def __init__(self):

        pass

class FlightVehicle(Vehicle): # FlightVehicle is the base class for Airplane and Starship

    def __init__(self):

        super(FlightVehicle, self).__init__()

        pass

class Airplane(FlightVehicle):

    def __init__(self):

        super(Airplane, self).__init__()

        pass
        
class Starship(FlightVehicle):

    def __init__(self):

        super(Starship, self).__init__()

        pass

class GroundVehicle(Vehicle): # GroundVehicle is the base class for Car and Motorcycle

    def __init__(self):

        super(GroundVehicle, self).__init__()

        pass

class Car(GroundVehicle):

    def __init__(self):

        super(Car, self).__init__()

        pass

class Motorcycle(GroundVehicle):

    def __init__(self):

        super(Motorcycle, self).__init__()

        pass