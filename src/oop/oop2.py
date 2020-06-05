
class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return f"vrooom"

class Motorcycle(GroundVehicle):
    def __init__(self):
        num_wheels = 2
        super().__init__(num_wheels)

    def drive(self):
        return f"BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

for item in vehicles:
    print(item.drive())
