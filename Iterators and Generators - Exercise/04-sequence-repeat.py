class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        index = self.i
        self.i += 1

        while index < self.number:
            find_idx = index % len(self.sequence)
            return self.sequence[find_idx]
        raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
