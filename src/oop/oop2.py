# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

    # TODO

class GroundVehicle():
    
    def __init__(self, **kwargs):
        self.num_wheels = kwargs['num_wheels'] if 'num_wheels' in kwargs else 4
        self.sound = kwargs['sound'] if 'sound' in kwargs else 'vroooom'
    
    def drive(self):
        return self.sound
    
    def num_wheels(self):
        return self.num_wheels

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


# TODO

class Motorcycle(GroundVehicle):
    def __init__(self, **kwargs):
        self.sound= 'BRAAAP!!'
        self.num_wheels= 2

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for i in vehicles:
    print(i.drive())