from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory("test", 5)

    def test_init(self):
        self.assertEqual("test", self.factory.name)
        self.assertEqual(5, self.factory.capacity)
        self.assertEqual( ["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)

    def test_add_ingredient_valid(self):
        self.factory.add_ingredient("white", 3)
        self.assertEqual({"white": 3}, self.factory.ingredients)

    def test_add_ingredient_existing_ingredient(self):
        self.factory.add_ingredient("white", 1)
        self.factory.add_ingredient("white", 3)
        self.assertEqual({"white": 4}, self.factory.ingredients)

    def test_add_ingredient_invalid_ingredient_expect_exception(self):
        with self.assertRaises(TypeError) as msg:
            self.factory.add_ingredient("black", 1)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(msg.exception))

    def test_add_ingredient_invalid_quantity_ingredient_expect_exception(self):
        with self.assertRaises(ValueError) as msg:
            self.factory.add_ingredient("white", 6)
        self.assertEqual("Not enough space in factory", str(msg.exception))

    def test_remove_ingredients_valid(self):
        self.factory.add_ingredient("white", 1)
        self.factory.remove_ingredient("white", 1)
        self.assertEqual({"white": 0}, self.factory.ingredients)

    def test_remove_ingredients_invalid_quantity_expect_exception(self):
        self.factory.add_ingredient("white", 1)
        with self.assertRaises(ValueError) as msg:
            self.factory.remove_ingredient("white", 2)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(msg.exception))

    def test_remove_ingredients_invalid_ingredient_expect_exception(self):
        with self.assertRaises(KeyError) as msg:
            self.factory.remove_ingredient("white", 1)
        self.assertEqual("'No such ingredient in the factory'", str(msg.exception))


if __name__ == "__main__":
    main()
