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
    def __init__(self, topSpeed):
        self.topSpeed = topSpeed

# Subclass of Vehicle, Super of Car / Motorcycle
# Is-a Vehicle, Has-a Car / Motorcycle
class GroundVehicle(Vehicle):
    def __init__(self, tires, topSpeed):
        super().__init__(topSpeed)
        self.tires = tires

# Subclass of Vehicle, Super of Airplane / Starship
# Is-a Vehicle, Has-a Airplane / Starship
class FlightVehicle(Vehicle):
    def __init__(self, pilots, topSpeed):
        super().__init__(topSpeed)
        self.pilots = pilots

    def __str__(self):
        return self.pilots
        
# Subclass of GroundVehicle
# Is-A GroundVehicle, Is-A Vehicle
class Car(GroundVehicle):
    def __init__(self, brand, fourWD, tires, topSpeed):
        super().__init__(tires, topSpeed)
        self.brand = brand
        self.fourWD = fourWD

# Subclass of GroundVehicle
# Is-A GroundVehicle, Is-A Vehicle
class Motorcycle(GroundVehicle):
    def __init__(self, brand, base, tires, topSpeed):
        super().__init__(tires,topSpeed)
        self.brand = brand
        self.base = base

# Subclass of FlightVehicle
# Is-A FlightVehicle, Is-A Vehicle
class Airplane(FlightVehicle):
    def __init__(self, brand, seatsPerRow, pilots, topSpeed):
        super().__init__(pilots,topSpeed)
        self.brand = brand
        self.seatsPerRow = seatsPerRow

# Subclass of FlightVehicle
# Is-A FlightVehicle, Is-A Vehicle
class Starship(FlightVehicle):
    def __init__(self, brand, familySpace, pilots, topSpeed):
        super().__init__(pilots, topSpeed)
        self.brand = brand
        self.familySpace = familySpace

car = Car("Mazda 3", False, 4, "110 mph")
mc = Motorcycle("Honda Shadow", "Chopper", 2, "150 mph")
plane = Airplane("Boeing 747", 8, 2, "10000 mph")
starship = Starship("Enterprise", 1000, 12, "701,748,755.636 mph at Max Warp Speed")
objs = [car,mc,plane,starship]

for obj in objs:
    print("\n%s" %obj.brand)
    underscore = ""
    seq = []
    for nothin in range(len(obj.brand)):
        seq.append("-")
    print(underscore.join(seq))
    for prop, value in vars(obj).items():
        print("{0:<15}: {1:<0}".format(prop, str(value)))
