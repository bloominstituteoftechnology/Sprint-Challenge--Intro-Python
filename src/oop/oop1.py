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
    def __init__(self, year = 2020, make = "None", model = "None", environment = "Anywhere"):
        self.year = year
        self.make = make 
        self.model = model
        self.environment = environment

class FlightVehicle(Vehicle):
    def __init__(self, year = 2020, make = "None", model = "None", maxHeight = 100, maxFuel = 50):
        super(FlightVehicle, self).__init__(year, make, model, "Air")
        self.maxHeight = maxHeight
        self.maxFuel = maxFuel
        self.currectFuelLevel = maxFuel
        self.currentHeight = 0
        self.isFlying = False

    def fly(self):
        self.isFlying = True
        self.currectFuelLevel -= 10
        self.currentHeight += 100
    
    def flyHeigher(self, height):
        if self.isFlying:
            self.currectFuelLevel -= height//10
            if self.currentHeight + height < self.maxHeight:
                self.currentHeight += height
            else:
                print("You can't fly that hight!")
        else:
            print("You are not flying yet.")

    def flyLower(self, height):
        if self.isFlying:
            self.currectFuelLevel -= height//10
            if self.currentHeight - height > 0:
                self.currentHeight -= height
            else:
                print("You can't fly that low!")
        else:
            print("You are not flying yet.")

    def land(self):
        if self.isFlying:
            self.currectFuelLevel -= 50
            self.isFlying = False
            self.currentHeight = 0
        else:
            print("You're already on land")


class Starship(FlightVehicle):
    def __init__(self, year = 2020, make = "None", model = "None", maxFuel = 500, maxSpeed = 10_000):
        super(Starship, self).__init__(year, make, model, float("inf"), maxFuel)
        self.maxSpeed = maxSpeed
        self.currentSpeed = 0


class Airplane(FlightVehicle):
    def __init__(self, year = 2020, make = "None", model = "None", maxHeight = 500, maxFuel = 250):
        super(Airplane, self).__init__(year, make, model, maxHeight, maxFuel)

class GroundVehicle(Vehicle):
    def __init__(self, year = 2020, make = "None", model = "None", numberOfWheels = 4):
        super(GroundVehicle, self).__init__(year, make, model, "Ground")
        self.numberOfWheels = numberOfWheels

class Car(GroundVehicle):
    def __init__(self, year = 2020, make = "None", model = "None"):
        super(Car, self).__init__(year, make, model, 4)

class Motorcycle(GroundVehicle):
    def __init__(self, year = 2020, make = "None", model = "None"):
        super(Motorcycle, self).__init__(year, make, model, 3)
