from unittest import TestCase
from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory


class TestPaintFactory(TestCase):
    name = "Test"
    capacity = 5

    def setUp(self):
        self.factory = PaintFactory(self.name, self.capacity)

    def test_init(self):
        self.assertEqual(self.name, self.factory.name)
        self.assertEqual(self.capacity, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_add_ingredient_with_valid_input(self):
        self.factory.add_ingredient("white", 3)
        self.assertEqual({"white": 3}, self.factory.ingredients)

    def test_add_ingredient_with_existing_ingredient_valid_quantity(self):
        self.factory.ingredients["white"] = 3
        self.assertEqual({"white": 3}, self.factory.ingredients)
        self.factory.add_ingredient("white", 1)
        self.assertEqual({"white": 4}, self.factory.ingredients)

    def test_add_ingredient_insufficient_capacity_expect_exception(self):
        self.factory.ingredients["yellow"] = 3
        with self.assertRaises(ValueError) as msg:
            self.factory.add_ingredient("yellow", 3)
        self.assertEqual( "Not enough space in factory", str(msg.exception))
        self.assertEqual({"yellow": 3}, self.factory.ingredients)

    def test_add_ingredient_invalid_ingredient_expect_exception(self):
        with self.assertRaises(TypeError) as msg:
            self.factory.add_ingredient("black", 1)
        self.assertEqual(f"Ingredient of type black not allowed in {type(self.factory).__name__}", str(msg.exception))

    def test_remove_ingredient_valid_input(self):
        self.factory.ingredients["white"] = 3
        self.factory.remove_ingredient("white", 2)
        self.assertEqual({"white": 1}, self.factory.ingredients)

    def test_remove_ingredient_quantity_too_much_expext_exception(self):
        self.factory.ingredients["white"] = 3
        with self.assertRaises(ValueError) as msg:
            self.factory.remove_ingredient("white", 5)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(msg.exception))

    def test_remove_ingredient_invalid_ingredient_type_expect_exception(self):
        with self.assertRaises(KeyError) as msg:
            self.factory.remove_ingredient("white", 1)
        self.assertEqual("'No such ingredient in the factory'", str(msg.exception))

    def test_product_property(self):
        self.factory.ingredients["white"] = 3
        self.assertEqual({"white": 3}, self.factory.products)

    def test_inheritance(self):
        self.assertIsInstance(self.factory, Factory)
        self.assertIsInstance(self.factory, PaintFactory)
        self.assertTrue(issubclass(PaintFactory, Factory))
