import unittest
from project.rooms.room import Room
from project.people.child import Child
from project.appliances.laptop import Laptop


class TestRoom(unittest.TestCase):
    name = "Simpson"
    budget = 1000
    members = 2

    def setUp(self):
        self.room = Room(self.name, self.budget, self.members)

    def test_init(self):
        self.assertEqual(self.name, self.room.family_name)
        self.assertEqual(self.budget, self.room.budget)
        self.assertEqual(self.members, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_props(self):
        self.room.expenses = 100
        self.assertEqual(100, self.room.expenses)

    def test_expenses_setter_expect_exception(self):
        with self.assertRaises(ValueError) as msg:
            self.room.expenses = -100
        self.assertEqual("Expenses cannot be negative", str(msg.exception))

    def test_calculate_expenses(self):
        child1 = Child(1, 2, 2)
        child2 = Child(3, 3, 4)
        laptop = Laptop()
        self.room.calculate_expenses([child1, child2], [laptop])
        result = child1.get_monthly_expense() + child2.get_monthly_expense() + laptop.get_monthly_expense()
        self.assertEqual(result, self.room.expenses)


if __name__ == '__main__':
    unittest.main()
