import unittest
import oop1


# used this as reference: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestOop1(unittest.TestCase):
    def test_vehicle(self):
        """ Does the Vehicle class exist? """
        try:
            self.test = oop1.Vehicle()
            self.assertIsInstance(self.test, oop1.Vehicle)
            print("\nVehicle Class Exists\n")
        except NameError as e:
            print(e)

    def test_flight_vehicle(self):
        """ Does the FlightVehicle class exist? """
        try:
            self.test = oop1.FlightVehicle()
            self.assertIsInstance(self.test, oop1.FlightVehicle)
            print("\nFlightVehicle Class Exists\n")
        except NameError as e:
            print(e)

    def test_ground_vehicle(self):
        """ Does the GroundVehicle class exist? """
        try:
            self.test = oop1.GroundVehicle()
            self.assertIsInstance(self.test, oop1.GroundVehicle)
            print("\nGroundVehicle Class Exists\n")
        except NameError as e:
            print(e)

    def test_starship(self):
        """ Does the Starship class exist? """
        try:
            self.test = oop1.Starship()
            self.assertIsInstance(self.test, oop1.Starship)
            print("\nStarship Class Exists\n")
        except NameError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()