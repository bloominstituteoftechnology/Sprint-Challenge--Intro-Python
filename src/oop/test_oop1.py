import unittest
import oop1


class Oop1Tests(unittest.TestCase):
    def setUp(self):
        self.vehicle = oop1.Vehicle()
        self.flight_vehicle = oop1.FlightVehicle()
        self.ground_vehicle = oop1.GroundVehicle()
        self.car = oop1.Car()
        self.motorcycle = oop1.Motorcycle()
        self.starship = oop1.Starship()
        self.airplane = oop1.Airplane()

    def test_flight_vehicle(self):
        print("flight", self.flight_vehicle)
        self.assertTrue(isinstance(self.flight_vehicle, oop1.FlightVehicle))
        self.assertTrue(isinstance(self.flight_vehicle, oop1.Vehicle))

    def test_ground_vehicle(self):
        self.assertTrue(isinstance(self.ground_vehicle, oop1.GroundVehicle))
        self.assertTrue(isinstance(self.ground_vehicle, oop1.Vehicle))

    def test_starship(self):
        self.assertTrue(isinstance(self.starship, oop1.Starship))
        self.assertTrue(isinstance(self.starship, oop1.FlightVehicle))
        self.assertTrue(isinstance(self.starship, oop1.Vehicle))

    def test_airplane(self):
        self.assertTrue(isinstance(self.airplane, oop1.Airplane))
        self.assertTrue(isinstance(self.airplane, oop1.FlightVehicle))
        self.assertTrue(isinstance(self.starship, oop1.Vehicle))

    def test_car(self):
        self.assertTrue(isinstance(self.car, oop1.Car))
        self.assertTrue(isinstance(self.car, oop1.GroundVehicle))
        self.assertTrue(isinstance(self.car, oop1.Vehicle))

    def test_motocycle(self):
        self.assertTrue(isinstance(self.motorcycle, oop1.Motorcycle))
        self.assertTrue(isinstance(self.motorcycle, oop1.GroundVehicle))
        self.assertTrue(isinstance(self.motorcycle, oop1.Vehicle))


if __name__ == '__main__':
    unittest.main()
