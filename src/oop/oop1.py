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
class Vehicle():
    pass

class FlightVehicle(Vehicle):
    #vehicle is the base class
    pass

class Airplane(FlightVehicle):
    # Flightvehicle is base class
    pass

class Starship(FlightVehicle):
    #FlightVehicle is base class
    pass

class GroundVehicle(Vehicle):
    # Vehicle is Base class
    pass

class Car(GroundVehicle):
    # GroundVehicle is base Class
    pass

class Motorcycle(GroundVehicle):
    #GroundVehicle is base class
    pass