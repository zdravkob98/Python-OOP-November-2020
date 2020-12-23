from CarManager.car_manager import Car

import unittest

class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('bmw', 'sedan', 5, 50)

    def test_set_init(self):
        self.assertEqual(self.car.make, 'bmw')
        self.assertEqual(self.car.model, 'sedan')
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 50)

    def test_make_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as exp:
            self.car.make = ''
        self.assertEqual(str(exp.exception), "Make cannot be null or empty!")

        with self.assertRaises(Exception) as exp:
            self.car.make = 0
        self.assertEqual(str(exp.exception), "Make cannot be null or empty!")

    def test_make(self):
        self.car.make = 'ford'
        self.assertEqual(self.car.make, 'ford')

    def test_model_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as exp:
            self.car.model = ''
        self.assertEqual(str(exp.exception), "Model cannot be null or empty!")

        with self.assertRaises(Exception) as exp:
            self.car.model = 0
        self.assertEqual(str(exp.exception), "Model cannot be null or empty!")

    def test_model(self):
        self.car.model = 'limozina'
        self.assertEqual(self.car.model, 'limozina')

    def test_fuel_consumption_cannot_be_zero_or_negative(self):
        with self.assertRaises(Exception) as exp:
            self.car.fuel_consumption = -42
        self.assertEqual(str(exp.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as exp:
            self.car.fuel_consumption = 0
        self.assertEqual(str(exp.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption(self):
        self.car.fuel_consumption = 10
        self.assertEqual(self.car.fuel_consumption, 10)

    def test_fuel_capacity_cannot_be_zero_or_negative(self):
        with self.assertRaises(Exception) as exp:
            self.car.fuel_capacity = -42
        self.assertEqual(str(exp.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as exp:
            self.car.fuel_capacity = 0
        self.assertEqual(str(exp.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity(self):
        self.car.fuel_capacity = 60
        self.assertEqual(self.car.fuel_capacity, 60)

    def test_fuel_amount_cannot_be_zero_or_negative(self):
        with self.assertRaises(Exception) as exp:
            self.car.fuel_amount = -42
        self.assertEqual(str(exp.exception), "Fuel amount cannot be negative!")

    def test_fuel_amount(self):
        self.car.fuel_amount = 10
        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel__cannot_be_zero_or_negative(self):
        with self.assertRaises(Exception) as exp:
            self.car.refuel(-42)
        self.assertEqual(str(exp.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as exp:
            self.car.refuel(0)
        self.assertEqual(str(exp.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_drive_without_fuel_raise(self):
        with self.assertRaises(Exception) as exp:
            self.car.drive(10)
        self.assertEqual(str(exp.exception), "You don't have enough fuel to drive!")

    def test_drive(self):
        self.car.fuel_amount = 5
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == '__main__':
    unittest.main()