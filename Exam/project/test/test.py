from project.pet_shop import PetShop
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self):
        self.shop = PetShop("test")

    def test_init(self):
        self.assertEqual("test", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_valid(self):
        actual = self.shop.add_food("whiskas", 200.0)
        expected = f"Successfully added 200.00 grams of whiskas."
        self.assertEqual({"whiskas": 200.0}, self.shop.food)
        self.assertEqual(expected, actual)

    def test_add_food_invalid_quantity_expect_exception(self):
        with self.assertRaises(Exception) as msg:
            actual = self.shop.add_food("whiskas", -200.0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(msg.exception))

    def test_add_food_valid_existing_food(self):
        actual = self.shop.add_food("whiskas", 200.0)
        expected = f"Successfully added 200.00 grams of whiskas."
        self.assertEqual({"whiskas": 200.0}, self.shop.food)
        self.assertEqual(expected, actual)
        actual = self.shop.add_food("whiskas", 100.0)
        expected = f"Successfully added 100.00 grams of whiskas."
        self.assertEqual({"whiskas": 300.0}, self.shop.food)
        self.assertEqual(expected, actual)

    def test_add_pet_valid(self):
        actual = self.shop.add_pet("parrot")
        expected = f"Successfully added parrot."
        self.assertEqual(expected, actual)
        self.assertEqual(["parrot"], self.shop.pets)

    def test_add_pet_existing_pet_expect_exception(self):
        self.shop.add_pet("parrot")
        with self.assertRaises(Exception) as msg:
            self.shop.add_pet("parrot")
        self.assertEqual("Cannot add a pet with the same name", str(msg.exception))

    def test_feed_pets_not_existing_pet_expect_exception(self):
        with self.assertRaises(Exception) as msg:
            self.shop.feed_pet("test_food", "test_pet")
        self.assertEqual("Please insert a valid pet name", str(msg.exception))

    def test_feed_pets_not_existing_food_expect_exception(self):
        self.shop.add_pet("parrot")
        actual = self.shop.feed_pet("test_food", "parrot")
        self.assertEqual("You do not have test_food", actual)

    def test_feed_pets_quantity_lt_100(self):
        self.shop.add_pet("cat")
        self.shop.add_food("whiskas", 50.0)
        actual = self.shop.feed_pet("whiskas", "cat")
        self.assertEqual("Adding food...", actual)
        self.assertEqual({"whiskas": 1050.0}, self.shop.food)

    def test_feed_pets_gt_100(self):
        self.shop.add_pet("cat")
        self.shop.add_food("whiskas", 500.0)
        actual = self.shop.feed_pet("whiskas", "cat")
        self.assertEqual("cat was successfully fed", actual)
        self.assertEqual({"whiskas": 400}, self.shop.food)

    def test_repr_method(self):
        self.shop.add_pet("cat")
        self.shop.add_pet("parrot")
        self.shop.add_food("whiskas", 500.0)
        expected = "Shop test:\nPets: cat, parrot"
        self.assertEqual(expected, self.shop.__repr__())


if __name__ == "__main__":
    main()