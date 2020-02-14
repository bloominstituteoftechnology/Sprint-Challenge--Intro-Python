# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels =4): # initialized method; w/ num_wheels defaults to 4
        self.num_wheels = num_wheels  # setting the instance variable

    # TODO
    def drive(self): # initialized drive() method
        return 'vroooom' # returns "vroooom".


# Subclass Motorcycle from GroundVehicle.
#

class Motorcycle(GroundVehicle): #inherits from GroundVehicle
    def __init__(self, num_wheels=None):
        super(). __init__(num_wheels = 2) # super, sets num_wheels defaults to 2
        pass
    def drive(self):  # initialized drive() method
        return "BRAAAP!!"  # returns "BRAAAP"


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

for i in vehicles: # goes thru vehicles list and print the result of calling drive() on each.
    print(i.drive())


