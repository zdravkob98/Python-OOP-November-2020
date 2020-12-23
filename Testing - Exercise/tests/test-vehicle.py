from solution.vehicle import Vehicle, Car, Truck

import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car(100, 3)

    def test_initialization(self):
        self.assertEqual(self.car.fuel_quantity, 100)
        self.assertEqual(self.car.fuel_consumption, 3)
        self.assertEqual(self.car.air_conditioners_consumption, 0.9)

    def test_drive_func_with_enough_fuel(self):
        self.car.drive(10)
        self.assertEqual(self.car.fuel_quantity, 61)

    def test_drive_func_without_fuel(self):
        self.car.drive(40)
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_refuel(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_quantity, 150)


class TruckTest(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100, 3)

    def test_initialization(self):
        self.assertEqual(self.truck.fuel_quantity, 100)
        self.assertEqual(self.truck.fuel_consumption, 3)
        self.assertEqual(self.truck.air_conditioners_consumption, 1.6)

    def test_drive_func_with_enough_fuel(self):
        self.truck.drive(15)
        self.assertEqual(self.truck.fuel_quantity, 31)

    def test_drive_func_without_fuel(self):
        self.truck.drive(30)
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_refuel(self):
        self.truck.refuel(20)
        self.assertEqual(self.truck.fuel_quantity,119)


if __name__ == '__main__':
    unittest.main()
