# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle():
    def __init__(self, num_wheels=4):
        self._num_wheels = num_wheels
        # self.num_wheels = num_wheels
    @property
    def num_wheels(self):
        return self._num_wheels
    # def print_wheels(self):
    #     print('num_wheels', self.num_wheels)

    def drive(self):
        return "vroooom"


class Motorcycle(GroundVehicle):
    def __init___(self, num_wheels=2):
        self._num_wheels = num_wheels
        super().__init__(self, num_wheels = self._num_wheels)
        # super(Motorcycle, self).__init__(self, num_wheels=num_wheels)
        # GroundVehicle().__init__(num_wheels=num_wheels)
        print('num_wheels  XXX')

    @property
    def num_wheels(self):
        return 2

    @num_wheels.setter 
    def num_wheels(self, w):
         self._num_wheels = w         

    def drive(self):
        return "BRAAAP!!"

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
    Motorcycle(2),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for v in vehicles:
    print(v.drive())


for v in vehicles:
    print(v.num_wheels)   
# print(GroundVehicle(2).num_wheels) 
print(Motorcycle().num_wheels)
