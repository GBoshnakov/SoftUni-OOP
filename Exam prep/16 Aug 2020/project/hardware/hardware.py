class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.available_memory = memory
        self.available_capacity = capacity

    def install(self, software):
        if not self.is_installable(software):
            raise Exception("Software cannot be installed")
        self.available_memory -= software.memory_consumption
        self.available_capacity -= software.capacity_consumption
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.available_memory += software.memory_consumption
            self.available_capacity += software.capacity_consumption

    def is_installable(self, software):
        if software.memory_consumption > self.available_memory or software.capacity_consumption > self.available_capacity:
            return False
        return True
