from worker import Worker
import unittest


class WorkerTest(unittest.TestCase):
    name = "Test"
    salary = 1000
    energy = 2

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_initializing(self):
        """Test if the worker is initialized with correct name, salary, and energy"""
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_energy_after_function_call(self):
        """Test if the worker's energy is incremented after the rest method is called"""
        expected = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected, self.worker.energy)

    def test_worker_if_energy_is_0__expect_exeption(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_money_after_work_method(self):
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary)
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary * 2)

    def test_if_worker_energy_decreases_after_work_method(self):
        """Test if the worker's energy is decreased after the work method is called"""
        expected = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(expected, self.worker.energy)

    def test_get_info_method(self):
        """Test if the get_info method returns the proper string with correct values"""
        expected = f'{self.name} has saved 0 money.'
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()