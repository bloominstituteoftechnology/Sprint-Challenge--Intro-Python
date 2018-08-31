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


# BASE CLASS

class Vehicle:
    def __init__(self, vId):
        self.vId = vId

# SUB-CLASSES

class GroundVehicle(Vehicle):
    def __init__(self, gVId, vId):
        super().__init__(vId)
        self.gVId = gVId

class Car(GroundVehicle):
    def __init__(self, cId, gVId):
        super().__init__(gVId)
        self.cId = cId

class Motorcycle(GroundVehicle):
    def __init__(self, mId, gVId):
        super().__init__(gVId)
        self.mId = mId


class FlightVehicle(Vehicle):
    def __init__(self, fVId, vId):
        super().__init__(vId)
        self.fVId = fVId

class Airplane(FlightVehicle):
    def __init__(self, aId, fVId):
        super().__init__(fVId)
        self.aId = aId


class Starship(Vehicle):
    def __init__(self, sId, vId):
        super().__init__(vId)
        self.sId

