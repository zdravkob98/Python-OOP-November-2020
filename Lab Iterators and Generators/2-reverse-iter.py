class reverse_iter:
    def __init__(self, iterator):
        self.iterator = iterator
        self.i = len(iterator) - 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            index = self.i
            self.i -= 1
            return self.iterator[index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
