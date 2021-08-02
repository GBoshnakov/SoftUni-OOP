from extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def test_init_with_integers(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], integer_list.get_data())

    def test_init_with_str_and_ints(self):
        integer_list = IntegerList(1, 2, "test")
        self.assertEqual([1, 2], integer_list.get_data())

    def test_init_with_floats(self):
        integer_list = IntegerList(1.5, 2.5, 3.5)
        self.assertEqual([], integer_list.get_data())

    def test_add_method_with_int(self):
        integer_list = IntegerList()
        actual = integer_list.add(10)
        self.assertEqual([10], actual)

    def test_add_method_with_str(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add("test")

    def test_remove_index_method_with_valid_index(self):
        integer_list = IntegerList(1, 2, 3)
        actual = integer_list.remove_index(1)
        self.assertEqual(2, actual)
        self.assertEqual(integer_list.get_data(), [1, 3])

    def test_remove_index_method_with_invalid_index__expect_exception(self):
        integer_list = IntegerList()
        with self.assertRaises(IndexError):
            integer_list.remove_index(1)

    def test_get_method_with_invalid_index(self):
        integer_list = IntegerList()
        with self.assertRaises(IndexError):
            integer_list.get(1)

    def test_get_method_with_valid_index(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(3, integer_list.get(2))

    def test_insert_method_with_valid_index(self):
        integer_list = IntegerList(1, 2)
        integer_list.insert(1, 100)
        self.assertEqual([1, 100, 2], integer_list.get_data())

    def test_insert_method_with_invalid_index__expect_exception(self):
        integer_list = IntegerList()
        with self.assertRaises(IndexError):
            integer_list.insert(1, 100)

    def test_insert_method_with_str__expect_exception(self):
        integer_list = IntegerList(1)
        with self.assertRaises(ValueError):
            integer_list.insert(0, "test")

    def test_get_biggest(self):
        biggest = 100
        integer_list = IntegerList(1, biggest, 2, 3 )
        self.assertEqual(biggest, integer_list.get_biggest())

    def test_get_index(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(2, integer_list.get_index(3))


if __name__ == "__main__":
    unittest.main()
