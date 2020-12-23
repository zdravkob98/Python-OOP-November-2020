from worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('zdravko', 1500, 100)

    def test_init(self):
        self.assertEqual(self.worker.name, 'zdravko')
        self.assertEqual(self.worker.salary, 1500)
        self.assertEqual(self.worker.energy, 100)

    def test_increment_energy_after_rest_method(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    def test_if_try_to_work_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as exp:
            self.worker.work()

        self.assertEqual(str(exp.exception), 'Not enough energy.')

    def test_if_try_to_work_with_negative_energy(self):
        self.worker.energy = -42
        with self.assertRaises(Exception) as exp:
            self.worker.work()

        self.assertEqual(str(exp.exception), 'Not enough energy.')

    def test_increase_money_after_work_method(self):
        self.worker.money = 0
        self.worker.work()
        self.assertEqual(self.worker.money, 1500)

    def test_decrease_energy_after_work_method(self):
        self.worker.energy = 10
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_correct_result_after_get_info(self):
        result = self.worker.get_info()
        expected_result = 'zdravko has saved 0 money.'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()