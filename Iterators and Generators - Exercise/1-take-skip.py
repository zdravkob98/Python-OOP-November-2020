class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.idx = 0
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        index = self.idx
        self.idx += 1

        while index <= self.count - 1:
            return index * self.step
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

