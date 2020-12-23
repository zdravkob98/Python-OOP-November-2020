from List.extended_list import IntegerList

import unittest

class IntegerListTest(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList([])

    def test_add_func(self):
        self.assertEqual(self.list.add(1), [1])

    def test_add_func_with_non_a_int(self):
        with self.assertRaises(ValueError) as exp:
            self.list.add('int')

        self.assertEqual(str(exp.exception), "Element is not Integer")

    def test_remove_func(self):
        self.list.add(1)
        el = self.list.remove_index(0)
        self.assertEqual(el, 1)

    def test_remove_func_with_index_error(self):
        with self.assertRaises(IndexError) as exp:
            self.list.remove_index(1)

        self.assertEqual(str(exp.exception), "Index is out of range")

    def test_get_func_must_return_element(self):
        self.list.add(2)
        self.assertEqual(self.list.get(0), 2)

    def test_get_func_out_of_range(self):
        with self.assertRaises(IndexError) as exp:
            self.list.get(0)

        self.assertEqual(str(exp.exception), "Index is out of range")

    def test_init_takes_only_ints(self):
        list = IntegerList('baba', 42, 'dqdo')
        self.assertEqual(list.get_data(), [42])

    def test_insert_func(self):
        with self.assertRaises(IndexError) as exp:
            self.list.insert(0, 1)
        self.assertEqual(str(exp.exception), "Index is out of range")

        self.list.add(1)
        with self.assertRaises(ValueError) as exp:
            self.list.insert(0, 'hello')
        self.assertEqual(str(exp.exception), "Element is not Integer")
        self.list.insert(0, 42)
        self.assertEqual(self.list.get_data(),[42, 1] )

    def test_get_biggest_func(self):
        self.list.add(1)
        self.list.add(10)
        self.assertEqual(self.list.get_biggest(), 10)

    def test_get_index_func(self):
        self.list.add(1)
        self.list.add(10)
        self.assertEqual(self.list.get_index(10), 1)


if __name__ == '__main__':
    unittest.main()