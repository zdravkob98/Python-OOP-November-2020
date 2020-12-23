import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceship(unittest.TestCase):
    def test_class_attribute(self):
        self.assertEqual(Spaceship.SPACESHIP_FULL, "Spaceship is full")
        self.assertEqual(Spaceship.ASTRONAUT_EXISTS, "Astronaut {} Exists")
        self.assertEqual(Spaceship.ASTRONAUT_NOT_FOUND, "Astronaut Not Found")
        self.assertEqual(Spaceship.ASTRONAUT_ADD, "Added astronaut {}")
        self.assertEqual(Spaceship.ASTRONAUT_REMOVED, "Removed {}")
        self.assertEqual(Spaceship.ZERO_CAPACITY, 0)

    def setUp(self) :
        self.spaceship = Spaceship('zdravko', 10)

    def test_init(self):
        self.spaceship = Spaceship('zdravko', 10)
        self.assertEqual(self.spaceship.name, 'zdravko')
        self.assertEqual(self.spaceship.capacity, 10)
        self.assertEqual(self.spaceship.astronauts, [])

    def test_add_raise_no_place(self):
        self.spaceship.capacity = 0
        with self.assertRaises(ValueError) as exp:
            self.spaceship.add('ivan')
        self.assertEqual(str(exp.exception), "Spaceship is full")

    def test_add_raise_the_same_person(self):
        self.spaceship.add('ivan')
        with self.assertRaises(ValueError) as exp:
            self.spaceship.add('ivan')
        self.assertEqual(str(exp.exception), "Astronaut ivan Exists")

    def test_add(self):
        self.spaceship.add('ivan')
        self.assertEqual(self.spaceship.astronauts, ['ivan'])

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as exp:
            self.spaceship.remove('ivan')
        self.assertEqual(str(exp.exception), "Astronaut Not Found")

    def test_remove(self):
        self.spaceship.add('ivan')
        self.spaceship.remove('ivan')
        self.assertEqual(self.spaceship.astronauts, [])


if __name__ == "__main__":
    unittest.main()