
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 1), 0)
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

    def test_add_two_numbers(self):
        self.assertEqual(self.calc.add_two_numbers(10, 5), 15)
        self.assertEqual(self.calc.add_two_numbers(-3, 3), 0)
        self.assertEqual(self.calc.add_two_numbers(0, 0), 0)

    def test_subtract_two_numbers(self):
        self.assertEqual(self.calc.subtract_two_numbers(10, 5), 5)
        self.assertEqual(self.calc.subtract_two_numbers(3, -3), 6)
        self.assertEqual(self.calc.subtract_two_numbers(0, 0), 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(3, -1), 1/3)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2)
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-4)

if __name__ == '__main__':
    unittest.main()
