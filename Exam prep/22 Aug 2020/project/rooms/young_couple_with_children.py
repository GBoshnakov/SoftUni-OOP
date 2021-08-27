from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    adult_room_members = 2

    def __init__(self, name, salary_one, salary_two, *children):
        members_count = self.adult_room_members + len(children)
        super().__init__(name, salary_one + salary_two, members_count)
        self.children = list(children)
        self.appliances = self.__create_appliances()
        self.calculate_expenses(self.appliances, self.children)

    def __create_appliances(self):
        appliances = []
        for _ in range(self.members_count):
            appliances.append(TV())
            appliances.append((Fridge()))
            appliances.append((Laptop()))
        return appliances

