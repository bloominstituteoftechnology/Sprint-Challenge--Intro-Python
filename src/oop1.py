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
	def __init__(self, name, kind, model):
		self.name = name
		self.kind = kind
		self.model = model

# sub-class of Vehicle
class FlightVehicle(Vehicle):
	def __init__(self, name, kind, model):
		super().__init__(name, kind, model)
		pass 

# sub-class of FlightVehicle
class Airplane(FlightVehicle):
	def __init__(self, name, kind, model):
		super().__init__(name, kind, model)
		pass

# sub-class of FlightVehicle
class Starship(FlightVehicle):
	def __init__(self, name, kind, model):
		super().__init__(name, kind, model)
		pass

# sub-class of Vehicle
class GroundVehicle(Vehicle):
	def __init__(self, name, kind, model):
		super().__init__(name, kind, model)
		pass

# sub-class of GroundVehicle
class Car(GroundVehicle):
	def __init__(self, name, kind, model):
		super().__init__(name, kind, model)
		pass

# sub-class of GroundVehicle
class Motorcycle(GroundVehicle):
	def __init__(self, name, kind, model):
		super().__init__(name, kind, model)
		pass
	
vehicle = Vehicle("submarine", "water vehicle", "model-A")
groundVehicle = GroundVehicle("bicycle", "ground vehicle", "model-B")
car = Car("toyota", "car", "model-c")
motorcycle = Motorcycle("harley", "motorcycle", "model-H")
flightVehicle = FlightVehicle("plane", "air vehicle", "model-P")
jet = Airplane("jet", "jet", "model-J")
starship = Starship("rocket", "rocket", "model-S")

print(vehicle.name, vehicle.kind, vehicle.model)
print(groundVehicle.name, groundVehicle.kind, groundVehicle.model)
print(car.name, car.kind, car.model)
print(motorcycle.name, motorcycle.kind, motorcycle.model)
print(flightVehicle.name, flightVehicle.kind, flightVehicle.model)
print(jet.name, jet.kind, jet.model)
print(starship.name, starship.kind, starship.model)




