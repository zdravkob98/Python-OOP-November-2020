from project.hardware.hardware import Hardware


class PowerHardware (Hardware):
    def __init__(self, name: str, capacity: int, memory):
        super().__init__(name, 'Power', capacity,memory)
        self.capacity = int(self.capacity * 0.25)
        self.memory = int(self.memory*1.75)



# p = PowerHardware('iii',1000, 100)
#
# print(p.name)
# print(p.type)
# print(p.capacity)
# print(p.memory)