class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __repr__(self):
         return self.name + ' ' + self.surname


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(name=None, people=self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __str__(self):
        return f'Group {self.name} with members {", ".join(map(str, [p for p in self.people]))}'

    def __getitem__(self, key: int):
        return f'Person {key}: {self.people[key]}'
