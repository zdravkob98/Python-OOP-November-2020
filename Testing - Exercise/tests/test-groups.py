from solution.groups import Person, Group

import unittest


class PersonTest(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('zdravko', 'bonev')
        self.person2 = Person('georgi', 'georgiev')

    def test_add_new_person(self):
        new_person = Person(self.person.name, self.person2.surname)

        self.assertEqual([new_person.name, new_person.surname], ['zdravko', 'georgiev'])

    def test_repr_method(self):
        self.assertEqual(self.person.__repr__(), self.person.name + ' ' + self.person.surname)


class GroupsTests(unittest.TestCase):
    def setUp(self) -> None:

        self.group = Group('first_group', people=[])
        self.group2 = Group('second_group', [])

    def test_add_group(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        p3 = Person('Elon', 'Musk')
        p4 = p3 + p2

        self.group = Group('first_group',[p0, p1, p2])
        self.group2 = Group('second_group',[p3, p4])
        group3 = self.group + self.group2
        self.assertEqual(len(group3), 5)

    def test_len(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        self.group = Group('first_group', [p0, p1, p2])

        self.assertEqual(self.group.__len__(), 3)

    def test_str(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        self.group = Group('first_group', [p0, p1, p2])

        self.assertEqual(self.group.__str__(), 'Group first_group with members Aliko Dangote, Bill Gates, Warren Buffet')

    def test_get_item(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        self.group = Group('first_group', [p0, p1, p2])
        key = 1

        self.assertEqual(self.group.__getitem__(key), f'Person {key}: {self.group.people[key]}')

    def test_geti_item_index_error(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        self.group = Group('first_group', [p0, p1, p2])
        key = 3
        with self.assertRaises(IndexError) as exp:
            self.group.__getitem__(key)

        self.assertEqual(str(exp.exception), 'list index out of range')


if __name__ == '__main__':
    unittest.main()