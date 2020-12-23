from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        a = [o for o in System._hardware if hardware_name == o.name]
        if a:
            inst = ExpressSoftware(name, capacity_consumption, memory_consumption)
            a[0].install(inst)
            if a[0].flag:
                System._software.append(inst)
            else:
                return "Software cannot be installed"
        else:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        a = [o for o in System._hardware if hardware_name == o.name]
        if a:
            inst = LightSoftware(name, capacity_consumption, memory_consumption)
            a[0].install(inst)
            if a[0].flag:
                System._software.append(inst)
            else:
                return "Software cannot be installed"
        else:
            return "Hardware does not exist"


    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        a = [o for o in System._hardware if o.name == hardware_name]
        b = [o for o in System._software if o.name == software_name]
        if a and b:
            a[0].uninstall(b[0])
            System._software.remove(b[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = []
        result.append(f'System Analysis')
        result.append(f'Hardware Components: {len(System._hardware)}')
        result.append(f'Software Components: {len(System._software)}')

        total_memory = sum([o.memory for o in System._hardware])
        total_used_memory = sum([o.memory_consumption for o in System._software])
        total_capacity = sum([o.capacity for o in System._hardware])
        total_used_capacity = sum([o.capacity_consumption for o in System._software])

        result.append(f'Total Operational Memory: {total_used_memory:.0f} / {total_memory:.0f}')
        result.append(f'Total Capacity Taken: {total_used_capacity:.0f} / {total_capacity:.0f}')
        return '\n'.join(result)

    # @staticmethod
    # def system_split():
    #     result = ''
    #     for hardware in System._hardware:
    #         result += f"Hardware Component - {hardware.name}\n"
    #
    #         number = len([software for software in hardware.software_components if
    #                       software.__class__.__name__ == "ExpressSoftware"])
    #         result += f"Express Software Components: {number}\n"
    #
    #         number = len([software for software in hardware.software_components if
    #                       software.__class__.__name__ == "LightSoftware"])
    #         result += f"Light Software Components: {number}\n"
    #
    #         used = sum([s.memory_consumption for s in hardware.software_components])
    #         result += f"Memory Usage: {used:.0f} / {hardware.memory:.0f}\n"
    #
    #         used = sum([s.capacity_consumption for s in hardware.software_components])
    #         result += f"Capacity Usage: {used:.0f} / {hardware.capacity:.0f}\n"
    #
    #         result += f"Type: {hardware.type}\n"
    #
    #         components = None if not hardware.software_components else ', '.join(
    #             software.name for software in hardware.software_components)
    #         result += f"Software Components: {components}"
    #     return result

    @staticmethod
    def system_split():
        result = []
        for component in System._hardware:
            result.append(f'Hardware Component - {component.name}')


            installed_component_express = len([c for c in component.software_components if c.__class__.__name__ == "ExpressSoftware"])
            result.append(f'Express Software Components: {installed_component_express}')

            installed_component_light = len([c for c in component.software_components if c.__class__.__name__ == "LightSoftware"])
            result.append(f'Light Software Components: {installed_component_light}')

            used_capacity = sum([c.memory_consumption for c in component.software_components])
            result.append(f'Memory Usage: {used_capacity:.0f} / {component.memory:.0f}')

            used_memory = sum([c.capacity_consumption for c in component.software_components])
            result.append(f'Capacity Usage: {used_memory:.0f} / {component.capacity:.0f}')

            result.append(f'Type: {component.type}')
            all_install_components = [c.name for c in component.software_components]
            if all_install_components:
                result.append(f'Software Components: {", ".join(map(str, all_install_components))}')
            else:
                result.append('None')
            return '\n'.join(result)