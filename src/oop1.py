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


class Vehicle(object):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __repr__(self):
        return """This is a base class """


class FlightVehicle(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self, name, speed)

    def __repr__(self):
        return """This is a subclass of Vehicle """


class Starship(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self, name, speed)

    def __repr__(self):
        return """This is a subclass of Vehicle """
#


class GroundVehicle(Vehicle):
    def __init__(self, name, speed):
        Vehicle.__init__(self, name, speed)

    def __repr__(self):
        return """This is a subclass of Vehicle """
#


class Car(GroundVehicle):
    def __init__(self, name, speed):
        GroundVehicle.__init__(self, name, speed)

    def __repr__(self):
        return """
        This is a subclass of GroundVehicle 
        This is a grandchild of Vehicle 
        
        """


class Motorcyle(GroundVehicle):
    def __init__(self, name, speed):
        GroundVehicle.__init__(self, name, speed)

    def __repr__(self):
        return """
        This is a subclass of GroundVehicle 
        This is a grandchild of Vehicle 
        
        """
#


class Airplane(FlightVehicle):
    def __init__(self, name, speed):
        FlightVehicle.__init__(self, name, speed)

    def __repr__(self):
        return """
        This is a subclass of FlightVehicle 
        This is a grandchild of Vehicle 
        
        """
#
