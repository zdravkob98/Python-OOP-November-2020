class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        if current_room:
            res = current_room.take_room(people)
            if not res:
                self.guests += current_room.guests

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        if current_room:
            people_for_remove = current_room.guests
            res = current_room.free_room()
            if res is None:
                self.guests -= people_for_remove


    def print_status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]

        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f"Free rooms: {', '.join(map(str, free_rooms))}")
        print(f"Taken rooms: {', '.join(map(str, taken_rooms))}")

