from cat import Cat

import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('sami')

    def test_init(self):
        self.assertEqual(self.cat.name, 'sami')

    def test_cat_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exp:
            self.cat.eat()
        self.assertEqual(str(exp.exception), 'Already fed.')

    def test_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as exp:
            self.cat.sleep()
        self.assertEqual(str(exp.exception), 'Cannot sleep while hungry')

    def test_cat_cannot_sleep_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)




if __name__ == '__main__':
    unittest.main()
