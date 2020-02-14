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

class Vehicle:
    """Base class for all the other class """
#    def __init__(self, motor, engine):
#        self.motor = motor
#        self.engine = engine
    pass

class FlightVehicle(Vehicle):
    """ Child class of Parent Vehicle """
#    def __init__(self, canfly):
#        super().__init__(motor, engine)
#        self.canfly = canfly
    pass

class Starship(FlightVehicle):
#    """Child class of Parent Vehicle class """
#    def __init__(self, gridfins, engines, booster, nozzle):
#        super().__init__(self, canfly)
#        self.gridfins = gridfins
#        self.engines = engines
#        self.booster = booster
#        self.nozzle = nozzle
    pass

class GroundVehicle(Vehicle):
    """Sub-child of Parent Vehicle class """
#    def __init__(self, tires, steeringwheel):
#        super().__init__(self, motor, engine)
#        self.tires = tires
#        self.steeringwheel = steeringwheel
    pass

class Car(GroundVehicle):
    """Sub-child of GroundVehicle parent class """
#    def __init__(self, fourtires):
#        super().__init__(self, tires, steeringwheel)
#        self.fourtires = fourtires
    pass

class Motorcycle(GroundVehicle):
#    """ child of GroundVehicle Parent"""
#    def __init__(self, twotires):
##        self.twotires = twotires
    pass

class Airplane(FlightVehicle):
    """Child of FlightVehicle Class """
#    def __init__(self, hasfins):
#        super().__init__(self, canfly)
#        self.hasfins = hasfins
    pass
