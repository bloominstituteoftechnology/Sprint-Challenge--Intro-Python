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


# Base class
class Vehicle:
	def __init__(self, engine):
		self.engine = engine

# Inherits from Vehicle class
class FlightVehicle(Vehicle):
	def __init__(self, engine, wings):
		Vehicle.__init__(self, engine)
		self.wings = wings

# Inherits from FlightVehicle class
class Airplane(FlightVehicle):
	def __init__(self, engine, wings, jetFuel):
		FlightVehicle.__init__(self, engine, wings)
		self.jetFuel = jetFuel

# Inherits from FlightVehicle class
class Starship(FlightVehicle):
	def __init__(self, engine, wings, nuclearFuel):
		FlightVehicle.__init__(self, engine, wings)
		self.nuclearFuel = nuclearFuel

# Inherits from Vehicle class
class GroundVehicle(Vehicle):
	def __init__(self, engine, gasolineFuel):
		Vehicle.__init__(self, engine)
		self.gasolineFuel = gasolineFuel

# Inherits from GroundVehicle class
class Car(GroundVehicle):
	def __init__(self, engine, gasolineFuel, fourWheels):
		GroundVehicle.__init__(self, engine, gasolineFuel)
		self.fourWheels = fourWheels

# Inherits from GroundVehicle class
class Motorcycle(GroundVehicle):
	def __init__(self, engine, gasolineFuel, twoWheels):
		self.twoWheels = twoWheels
