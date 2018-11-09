import unittest
import oop1


# used this as reference: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestOop1(unittest.TestCase):
    def test_vehicle(self):
        """ Does the Vehicle class exist? """
        try:
            self.test = oop1.Vehicle()
            self.assertIsInstance(self.test, oop1.Vehicle)
            print("\nPASS : Vehicle Class Exists\n")
        except NameError as e:
            print(e)

    def test_flight_vehicle(self):
        """ Does the FlightVehicle class exist? """
        try:
            self.test = oop1.FlightVehicle()
            self.assertIsInstance(self.test, oop1.FlightVehicle)
            print("\nPASS : FlightVehicle Class Exists\n")
        except NameError as e:
            print(e)

    def test_ground_vehicle(self):
        """ Does the GroundVehicle class exist? """
        try:
            self.test = oop1.GroundVehicle()
            self.assertIsInstance(self.test, oop1.GroundVehicle)
            print("\nPASS : GroundVehicle Class Exists\n")
        except NameError as e:
            print(e)

    def test_starship(self):
        """ Does the Starship class exist? """
        try:
            self.test = oop1.Starship()
            self.assertIsInstance(self.test, oop1.Starship)
            print("\nPASS : Starship Class Exists\n")
        except NameError as e:
            print(e)

    def test_airplane(self):
        """ Does the Airplane class exist? """
        try:
            self.test = oop1.Airplane()
            self.assertIsInstance(self.test, oop1.Airplane)
            print("\nPASS : Airplane Class Exists\n")
        except NameError as e:
            print(e)

    def test_car(self):
        """ Does the Car class exist? """
        try:
            self.test = oop1.Car()
            self.assertIsInstance(self.test, oop1.Car)
            print("\nPASS : Car Class Exists\n")
        except NameError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()