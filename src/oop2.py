# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

print("-------------------------------------------------------------")

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels
        print(f"This is a ground vehicle with {self.num_wheels} wheels")
        print("-------------------------------------------------------------")

    def drive(self):
        print("vroooom")    

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        super().__init__(num_wheels)
        print(f"This is a ground vehicle with {self.num_wheels} wheels")
        print("-------------------------------------------------------------")

    def drive(self):
        print("BRAAAP!!")    


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.
print("-------------------------------------------------------------")

r = [vehicle.drive() for vehicle in vehicles]  
print(r)

print("-------------------------------------------------------------")

# r = [f" The ground vehicle with {vehicle.num_wheels} goes {vehicle.drive()}" for vehicle in vehicles]  # TODO
# print(r)

