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
Class Vehicle(Vehicle, FlightVehicle, Starship): #base class/Super class
    def __init__(self, type)
        self.type = typeOf # type of vehicle
        self.FlightVehicle = flight 
        self.Starship = starship
        self.Vehicle = ground

Class GroundVehicle(Vehicle)
    def __init__ (self, type)
        self.type
        super().__init__("ground") #ask ? about this one.. 


