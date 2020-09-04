# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4, sound='vroooooom'):
        self.num_wheels = num_wheels
        self.sound = sound

    def drive(self):
        return f'{self.sound}'

    # TODO


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2, sound="BRAAAAP!!"):
        self.num_wheels = num_wheels
        self.sound = sound

    def drive(self):
        return f'{self.sound}'
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

for v in vehicles:
    print(v.drive())

x = [w.num_wheels for w in vehicles]
print(x)

# TODO

'''
python src/oop/oop2.py
'''