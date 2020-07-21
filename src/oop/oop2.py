# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self,sound='vrooom'):
        self.num_wheels = 4
        self.sound = sound
    def drive(self):
        print(self.sound)

class Motorcycle(GroundVehicle):
    def __init__ (self):
        super().__init__('BRAAP!!')
        self.num_wheels  = 2

    #def drive(self):
    #    print('BRAAAP!!')

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for x in vehicles:
    x.drive()

#vehicle = GroundVehicle()
#moto = Motorcycle()

#vehicle.drive()
#moto.drive()
#print(moto.num_wheels)