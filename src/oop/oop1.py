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

    def __init__(self, name):
        self.name = name
    
    def vehicle_name(self):
        print("Hello I am a " + self.name)

class GroundVehicle(Vehicle):
    pass
car = Vehicle("car")
motorcycle = Vehicle("motorcycle")
print(car, type(car))
print(motorcycle, type(motorcycle))
car.vehicle_name()
motorcycle.vehicle_name()


class FlightVehicle(Vehicle):
    pass
airplane = Vehicle("airplane")
starship = Vehicle("starship")
print(airplane, type(airplane))
airplane.vehicle_name()
print(starship, type(starship))
starship.vehicle_name()

