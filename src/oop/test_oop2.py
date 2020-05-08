import unittest
import oop2


class Oop2Tests(unittest.TestCase):
    def setUp(self):
        self.ground_vehicle = oop2.GroundVehicle()
        self.motorcycle = oop2.Motorcycle()

    def test_motorcycle_inheritance(self):
        self.assertTrue(isinstance(self.motorcycle, oop2.GroundVehicle))

    def test_ground_vehicle_num_wheels(self):
        self.assertEqual(self.ground_vehicle.num_wheels, 4)

    def test_motocycle_num_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_ground_vehicle_drive(self):
        self.assertEqual(self.ground_vehicle.drive(), "vroooom")

    def test_motorcyle_drive(self):
        self.assertEqual(self.motorcycle.drive(), "BRAAAP!!")


if __name__ == '__main__':
    unittest.main()
