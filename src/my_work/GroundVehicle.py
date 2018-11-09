from Car import Car
from Motorcycle import Motorcycle


class GroundVehicle:
    def __init__(self, name, num_wheels):
        self.name = name
        self.num_wheels = num_wheels
    
    def drive(self, sound):
        if sound == True:
            print("vroooom")
        else:
            print(f"{self.name} is not on.")

    def wheels(self):
        if self.motorcycle == True:
            num_wheels == '2'
        else:
            num_wheels == '4'
        print(f"{self.num_wheels}")
