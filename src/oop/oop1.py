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
    def __init__(self, year = 3000, make = "nil", model = "nil", environment = "any"):
         self.year = year
         self.make = make 
         self.model = model 
         self.environment = environment 


class FlightVehicle(Vehicle):
    def __init__(self, year = 3200, make = "black hawk", model = "death star", top_speed = 1000, top_height = 2000, fuel_load = 200):
         super(FlightVehicle, self).__init__(year, make, model, "Air") #env
         self.top_speed = top_speed
         self.top_height = top_height
         self.fuel_oad = fuel_load


class Starship(FlightVehicle):
    def __init__(self, year = 2020, make = "nil", model = "nil", top_speed = 3000, top_height = "nil"):
        super(Starship, self).__init__(year, make, model, top_speed, top_height)

class Airplane(FlightVehicle):
    def __init__(self, year = 2030, make = "nil", model = "nil", top_speed = 100, top_height = 1500):
        super(Airplane, self).__init__(year, make, model, top_speed, top_height)

class GroundVehicle(Vehicle):
    def __init__(self, year = 2020, make = "nil", model = "nil", numberOfWheels = 4):
        super(GroundVehicle, self).__init__(year, make, model, "Ground") #env
        self.numberOfWheels = numberOfWheels

class Car(GroundVehicle):
    def __init__(self, year = 2020, make = "nil", model = "nil"):
        super(Car, self).__init__(year, make, model, 4)

class Motorcycle(GroundVehicle):
    def __init__(self, year = 2020, make = "nil", model = "nil"):
        super(Motorcycle, self).__init__(year, make, model, 3)