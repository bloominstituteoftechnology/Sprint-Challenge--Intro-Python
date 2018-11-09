import unittest
import oop1


# used this as reference: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestOop1(unittest.TestCase):
    def test_vehicle(self):
        """ Does the class exist? """
        try:
            self.test = oop1.Vehicle()
            self.assertIsInstance(self.test, oop1.Vehicle)
            print("test passed!")
        except NameError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()