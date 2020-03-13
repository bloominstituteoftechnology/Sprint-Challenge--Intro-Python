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
    # the Vehicle class is the base class
    pass

# the 'flying' classes ultimate roll up and in to the vehicle class

class FlightVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass

# The ground vehicle class and its child classes ultimately roll up to the vehicle class

class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass