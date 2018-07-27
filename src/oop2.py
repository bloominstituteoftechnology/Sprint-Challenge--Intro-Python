# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels

    def drive(self):
        print("Vroom")


# Subclass Motorcycle from Vehicle.
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels
        super().__init__(num_wheels = 2)

    def drive(self):
        print("BRAAAP!!")

#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"


vehicles = [
    GroundVehicle(0),
    GroundVehicle(0),
    Motorcycle(0),
    GroundVehicle(0),
    Motorcycle(0),
]

# Go through the vehicles list and call drive() on each.


#TESTING BELOW

# for car in vehicles:
#     car.drive()
#     print(car.num_wheels)