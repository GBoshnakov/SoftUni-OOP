from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    room_cost = 20
    room_members = 2
    appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, name, salary_one, salary_two):
        super().__init__(name, salary_one + salary_two, YoungCouple.room_members)
        self.calculate_expenses(self.appliances)