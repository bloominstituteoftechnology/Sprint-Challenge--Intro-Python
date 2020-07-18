# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, sound, num_wheels=4):
        self.sound = sound
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        return GroundVehicle.drive
      
      



# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels, sound):
        self.num_wheels = num_wheels
        self.sound = sound

    def drive(self):
        return Motorcycle.drive

  
      


# TODO

sound = "vrooom"

vehicles = [
    GroundVehicle(4,"vrooom"),
    GroundVehicle(4,"vrooom"),
    Motorcycle(2,"Braaap!"),
    GroundVehicle(4,"vrooom"),
    Motorcycle(2,"Braaap!"),
]

# Go through the vehicles list and print the result of calling drive() on each.
print(GroundVehicle)
print(Motorcycle)

# TODO
