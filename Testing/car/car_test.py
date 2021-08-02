from car_manager import Car
import unittest


class TestCar(unittest.TestCase):
    make = "BMW"
    model = "330d"
    fuel_consumption = 10
    fuel_capacity = 70

    def test_constructor(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(self.make, car.make)
        self.assertEqual(self.model, car.model)
        self.assertEqual(self.fuel_consumption, car.fuel_consumption)
        self.assertEqual(self.fuel_capacity, car.fuel_capacity)

    def test_make_setter(self):
        with self.assertRaises(Exception):
            Car("", self.model, self.fuel_consumption, self.fuel_capacity)

    def test_model_setter(self):
        with self.assertRaises(Exception):
            Car(self.make, None, self.fuel_consumption, self.fuel_capacity)

    def test_fuel_consumption_setter(self):
        with self.assertRaises(Exception):
             Car(self.make, self.model, -50, self.fuel_capacity)

    def test_fuel_capacity_setter(self):
        with self.assertRaises(Exception):
            Car(self.make, self.model, self.fuel_consumption, -1)

    def test_fuel_amount_setter(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_amount = -10

    def test_refuel_method_with_negative_integer__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(-10)

    def test_refuel_method_with_integer_gt_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(75)
        self.assertEqual(self.fuel_capacity, car.fuel_amount)

    def test_refuel_method_with_int_lt_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(10)
        self.assertEqual(10, car.fuel_amount)

    def test_drive_method_with_insufficient_fuel(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(10)
        with self.assertRaises(Exception):
            car.drive(200)

    def test_drive_method_with_sufficient_fuel(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(10)
        car.drive(50)
        self.assertEqual(5, car.fuel_amount)


if __name__ == '__main__':
    unittest.main()