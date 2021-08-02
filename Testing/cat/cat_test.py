from cat import Cat
import unittest


class CatTest(unittest.TestCase):
    name = "Puss"

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_size_after_eat_method(self):
        """Cat's size is increased after eating"""
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_if_cat_is_fed_after_eat_method(self):
        """Cat is fed after eating"""
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_cat_eat__expect_exception(self):
        """Cat cannot eat if already fed, raises an error"""
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_if_cat_eats_when_not_fed(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_if_cat_sleepy_after_sleep_method__expect_exception(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()