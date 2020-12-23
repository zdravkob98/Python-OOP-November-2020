import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('sunny', 500, 2)

    def test_init(self):
        self.assertEqual(self.room.family_name, 'sunny')
        self.assertEqual(self.room.budget, 500)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_expenses(self):
        self.room.expenses = 0
        self.assertEqual(self.room.expenses, 0)
        self.room.expenses = 10
        self.assertEqual(self.room.expenses, 10)

    def test_expenses_raise(self):
        with self.assertRaises(ValueError) as exp:
            self.room.expenses = -1

        self.assertEqual(str(exp.exception), "Expenses cannot be negative")

if __name__ == '__main__':
    unittest.main()
