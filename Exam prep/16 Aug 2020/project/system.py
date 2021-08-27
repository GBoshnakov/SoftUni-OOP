from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [el for el in System._hardware if el.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(software)
            System._software.append(software)
        except Exception as msg:
            return str(msg)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [el for el in System._hardware if el.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(software)
            System._software.append(software)
        except Exception as msg:
            return str(msg)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [el for el in System._hardware if el.name == hardware_name]
        software = [el for el in System._software if el.name == software_name]
        if hardware and software:
            hardware[0].uninstall(software[0])
            System._software.remove(software[0])
            return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = f"System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {sum([el.memory for el in System._hardware]) - sum([el.available_memory for el in System._hardware])} / {sum([el.memory for el in System._hardware])}\n" \
                 f"Total Capacity Taken: {sum([el.capacity for el in System._hardware]) - sum([el.available_capacity for el in System._hardware])} / {sum([el.capacity for el in System._hardware])}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for component in System._hardware:
            result += f"Hardware Component - {component.name}\n" \
                     f"Express Software Components: {len([el for el in component.software_components if type(el).__name__ == 'ExpressSoftware'])}\n" \
                     f"Light Software Components: {len([el for el in component.software_components if type(el).__name__ == 'LightSoftware'])}\n" \
                     f"Memory Usage: {component.memory - component.available_memory} / {component.memory}\n" \
                     f"Capacity Usage: {component.capacity - component.available_capacity} / {component.capacity}\n" \
                     f"Type: {component.type}\n"
            soft_comps = [el.name for el in component.software_components]
            result += f"Software Components: {', '.join(soft_comps) if soft_comps else None}"

        return result
