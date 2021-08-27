from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware("RTX", "GPU", 100, 1000)
        self.software = Software("Nvidia", "driver", 50, 500)
        self.software2 = Software("Windows", "system", 1000, 5000)

    def test_init(self):
        self.assertEqual("RTX", self.hardware.name)
        self.assertEqual("GPU", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(1000, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_install_valid(self):
        self.hardware.install(self.software)
        self.assertEqual([self.software], self.hardware.software_components)
        self.assertEqual(100-50, self.hardware.available_capacity)
        self.assertEqual(1000-500, self.hardware.available_memory)

    def test_install_invalid_expect_exception(self):
        with self.assertRaises(Exception) as msg:
            self.hardware.install(self.software2)
        self.assertEqual("Software cannot be installed", str(msg.exception))

    def test_uninstall(self):
        self.hardware.install(self.software)
        self.assertEqual([self.software], self.hardware.software_components)
        self.hardware.uninstall(self.software)
        self.assertEqual([], self.hardware.software_components)


if __name__ == "__main__":
    main()