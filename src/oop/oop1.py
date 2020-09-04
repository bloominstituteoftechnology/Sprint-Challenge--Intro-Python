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
	#base class for all vehicles
	pass


class FlightVehicle(Vehicle):
	# base class to starship and Airplane
    pass

class Starship(FlightVehicle):
	pass

class Airplane(FlightVehicle):
	pass


class GroundVehicle(Vehicle):
	# base class for car and motorcycle
    
    pass

class Car(GroundVehicle):
	pass

class Motorcycle(GroundVehicle):
	pass
