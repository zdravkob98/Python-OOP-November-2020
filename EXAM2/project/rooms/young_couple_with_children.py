from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren (Room):
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        for _ in range(len(children)):
            self.appliances.append(TV())
            self.appliances.append(Fridge())
            self.appliances.append(Laptop())
        self.calculate_expenses(self.appliances, children)
