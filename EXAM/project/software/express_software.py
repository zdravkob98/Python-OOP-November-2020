from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, 'Express', capacity_consumption, memory_consumption)
        self.memory_consumption = int(self.memory_consumption * 2)


# c = ExpressSoftware('heloo', 1000, 2000)
# print(c.name)
# print(c.memory_consumption)
# print(c.capacity_consumption)
# print(c.type)
