import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    fuel = 10.0
    horse_power = 100.0

    def setUp(self):
        self.car = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.car.fuel)
        self.assertEqual(self.horse_power, self.car.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)
        self.assertEqual(self.fuel, self.car.capacity)

    def test_if_capacity_changes(self):
        self.assertEqual(self.fuel, self.car.capacity)
        self.car.fuel = 5
        self.assertEqual(self.fuel, self.car.capacity)

    def test_drive_method_insufficient_fuel__expect_exception(self):
        with self.assertRaises(Exception) as msg:
            self.car.drive(20)
        self.assertEqual("Not enough fuel", str(msg.exception))

    def test_drive_method_sufficient_fuel(self):
        self.car.drive(5)
        expected_fuel = self.fuel - (5 * self.car.fuel_consumption)
        self.assertEqual(expected_fuel, self.car.fuel)

    def test_refuel_too_much_fuel_expect_exception(self):
        with self.assertRaises(Exception) as msg:
            self.car.refuel(1)
        self.assertEqual("Too much fuel", str(msg.exception))

    def test_refuel_enough_capacity(self):
        self.car.drive(1)
        self.car.refuel(1)
        expected = self.fuel - (self.car.fuel_consumption * 1) + 1
        self.assertEqual(expected, self.car.fuel)

    def test_str_method(self):
        expected = f"The vehicle has {self.horse_power} " \
                   f"horse power with {self.fuel} fuel left and {Vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, str(self.car))
