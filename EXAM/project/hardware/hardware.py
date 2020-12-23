# from software.light_software import LightSoftware
from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.flag = False
        self.used_capacity = 0
        self.used_memory = 0

    def install(self, software: Software):
        try:
            if software.capacity_consumption + self.used_capacity <= self.capacity and software.memory_consumption + self.used_memory <= self.memory:
                self.used_capacity += software.capacity_consumption
                self.used_memory += software.memory_consumption
                self.software_components.append(software)
                self.flag = True
            else:
                raise Exception
        except Exception:
            self.flag = False
            return "Software cannot be installed"

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)


# h = Hardware('SSd', "ssss", 150, 500)
# c = LightSoftware('heloo', 10050, 40)
# # # print(c.name)
# # # print(c.memory_consumption)
# # # print(c.capacity_consumption)
# # # print(c.type)
# #
# print(h.install(c))
# print(h.flag)
# # # h.uninstall(c)
