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

#main class named Vehicle
class Vehicle:
    def __init__(self, type, terrain):
        self.type = type
        self.terrain = terrain

    def getType(self):
        return self.type

    def getTerrain(self):
        return self.terrain

    def __str__(self):
        return "%s is a %s vehicle" % (self.type, self.terrain)

#Ground vehicle subclass of vehicle class
class GroundVehicle(Vehicle):
    def __init__(self, type, color):
        super().__init__("ground")
        self.type = type
        self.color = color

        #instance of ground vehicle called car
        GroundVehicle("car", "Blue")
        #instance of ground vehicle called motorcycle
        GroundVehicle("motorcycle", "Orange")

#flightVehicle sub class of vehicle class
class FlightVehicle(Vehicle):
    def __init__(self, type, wingsAmount):
        super().__init__("air")
        self.type = type
        self.wingsAmount = wingsAmount

        #instance of flight vehicle called bi plane
        FlightVehicle("Bi-plane", 4)
                #instance of flight vehicle called helicopter
        FlightVehicle("Helicopter", 0)

#star ship sub class of vehicle class. 
class StarShip(Vehicle):
    def __init__(self, type, capacity):
        super().__init__("air")
        self.type = type
        self.capacity = capacity

        #transit instance of starship subclass
        StarShip("transit", 1000)
        StarShip("battleship", 900)
