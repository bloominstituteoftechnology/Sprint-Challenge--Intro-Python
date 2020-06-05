# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
    def __init__(self, num_wheels, drive):
        self.num_wheels = num_wheels
        self.drive = drive
#    @vroooommethod
    def drive(self):
        return ("vroooom")




class Motorcycle(GroundVehicle):
    def __init__(self,num_wheels, drive):
        super().__init__(num_wheels, drive)
        self.num_wheels = num_wheels
        self.drive = drive

bike = Motorcycle(2, "BRAAAP!!")
print(bike.num_wheels)
print(bike.drive)

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]
