# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
    def __init__(self, name, num_wheels=4):
        self.name = name
        self.num_wheels = num_wheels

    def __repr___(self):
        return f'{self.name} has {self.num_wheels} wheels'

    # TODO
    def drive(self):
        return "vrooom"
      
      



# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__(name, num_wheels =2)
      

    def drive(self):
        return "BRAAAP!!"

  
    
# TODO


vehicles = [
    GroundVehicle("Toyota"),
    GroundVehicle("Nissan"),
    Motorcycle("Harley"),
    GroundVehicle("Ford"),
    Motorcycle("Dirt Bike"),
]

# Go through the vehicles list and print the result of calling drive() on each.
print(GroundVehicle)
print(Motorcycle)

# TODO

for v in vehicles:
    print(v.drive())
