from solution.account import Account

import unittest

class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account('bob', 1000)

    def test_init(self):
        self.assertEqual(self.account.owner, 'bob')
        self.assertEqual(self.account.amount, 1000)
        self.assertEqual(self.account._transactions, [])

    def test_add_transaction_raise(self):
        with self.assertRaises(ValueError) as exp:
            self.account.add_transaction('sto')

        self.assertEqual(str(exp.exception), "please use int for amount")

    def test_add_transaction(self):
        self.account.add_transaction(500)
        self.assertEqual(self.account._transactions, [500])

    def test_balance(self):
        self.account.add_transaction(500)
        self.account.add_transaction(500)
        self.assertEqual(self.account.balance, 2000)

    def test_validation_transaction_raise(self):
        self.account.add_transaction(500)
        self.account.add_transaction(500)
        with self.assertRaises(ValueError) as exp:
            self.account.validate_transaction(self.account, -2500)

        self.assertEqual(str(exp.exception), 'sorry cannot go in debt!')

    def test_validation_transaction(self):
        result = self.account.validate_transaction(self.account, 250)
        self.assertEqual(self.account._transactions, [250])
        self.assertEqual(result, 'New balance: 1250')

    def test_str(self):
        self.assertEqual(self.account.__str__(), 'Account of bob with starting amount: 1000')

    def test_repr(self):
        self.assertEqual(self.account.__repr__(), 'Account(bob, 1000)')

    def test_len(self):
        self.assertEqual(self.account.__len__(), 0)

    def test_get_item(self):
        self.account.add_transaction(500)
        self.account.add_transaction(500)
        self.assertEqual(self.account.__getitem__(0), 500)

    def test_get_item_raise(self):
        with self.assertRaises(Exception) as exp:
            self.account.__getitem__(0)

        self.assertEqual(str(exp.exception), 'list index out of range')

    def test_gt(self):
        #1000
        other = Account('mariq', 500)
        other.add_transaction(50)

        self.assertTrue(self.account > other)
        self.assertTrue(self.account >= other)
        self.assertTrue(other >= other)
        self.assertTrue(self.account >= self.account)
        self.assertTrue(self.account != other)

        self.assertFalse(self.account < other)
        self.assertFalse(self.account <= other)
        self.assertFalse(self.account == other)

    def test_add_(self):
        other = Account('mariq', 500)
        other.add_transaction(500)
        self.account.add_transaction(1000)

        new_account = self.account + other
        self.assertEqual(new_account.amount, 1500)
        self.assertEqual(new_account.owner, 'bob&mariq')
        self.assertEqual(new_account._transactions, [1000, 500])

    def test_custom_reversed(self):
        self.account.add_transaction(500)
        self.account.add_transaction(150)
        result = list(reversed(self.account))
        self.assertEqual(result, [150, 500])

if __name__ == '__main__':
    unittest.main()