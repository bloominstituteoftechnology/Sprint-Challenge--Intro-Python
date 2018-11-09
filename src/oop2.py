# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
  def __init__(self, num_wheels=4):
    self.num_wheels = num_wheels
  def drive(self):
    print("vroooom")
  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)

class Motorcycle(GroundVehicle):
  def __init__(self, num_wheels=2):
    super().__init__(num_wheels)
  def drive(self):
    print("BRAAAP!!")

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle().drive(),
    GroundVehicle().drive(),
    Motorcycle().drive(),
    GroundVehicle().drive(),
    Motorcycle().drive(),
]
