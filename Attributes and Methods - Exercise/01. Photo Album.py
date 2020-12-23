class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]
        self.current_page = 0
        self.current_slot = 0
        self.page = 1

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label:str):
        if self.current_page >= self.pages:
            return "No more free spots"
        self.photos[self.current_page].append(label)

        if self.current_slot == 4:
            self.current_slot = 0
            self.page += 1
        if self.current_slot == 3:
            self.current_page += 1

        self.current_slot += 1

        return f"{label} photo added successfully on page {self.page} slot {self.current_slot}"


    def display(self):
        result = ''
        board = f"{'-' * 11}\n"
        body = ''

        result += board

        for i in range(self.pages):
            body = f"{'[] ' * len(self.photos[i])}"
            result += body[:-1] + '\n'
            result += board

        return result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


