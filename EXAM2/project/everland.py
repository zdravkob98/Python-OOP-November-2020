from project.people.child import Child
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget < room.expenses + room.room_cost:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
            else:
                result.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= room.expenses + room.room_cost
        return '\n'.join(result)


    def status(self):
        result = []
        people = sum([r.members_count for r in self.rooms])
        result.append(f"Total population: {people}")
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            total = 0
            if room.children:
                for n, c in enumerate(room.children):
                    child_cost = c.cost * 30
                    total += child_cost
                    n += 1
                    result.append(f"--- Child {n} monthly cost: {child_cost:.2f}$")
            result.append(f"--- Appliances monthly cost: {room.expenses - total:.2f}$")

        return '\n'.join(result)

everland = Everland()


young_couple = YoungCouple("Johnsons", 150, 205)

child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

everland.add_room(young_couple)
everland.add_room(young_couple_with_children)

print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())
