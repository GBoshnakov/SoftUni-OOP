import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    name = "Rex"
    animal_type = "dog"
    sound = "bark"

    def setUp(self):
        self.mammal = Mammal(self.name, self.animal_type, self.sound)

    def test_init(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.animal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected = f"{self.name} makes {self.sound}"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        expected = f"{self.name} is of type {self.animal_type}"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)