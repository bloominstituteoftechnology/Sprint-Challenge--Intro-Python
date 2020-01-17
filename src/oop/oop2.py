# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


class GroundVehicle():
    def __init__(self):
        self.num_wheels = 4  # setting number of wheels to 4 on a ground vehicle

    def drive(self):  # drive method returning "vrooom"
        return "vroooom"


class Motorcycle(GroundVehicle):  # passing down GroundVehicle into Motorcycle to inherit
    def __init__(self):
        self.num_wheels = 2  # overriding the original vehicle numbers to 2

    def drive(self):  # overwriting the drive method to return brap instead of vroom
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

for car in vehicles:
    print(car.drive)

# this is a loop that picks each car in the list of vehicles, goes through each vehicle and returns the drive method on each vehicle in the list.
