from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    room_members = 2
    appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]

    def __init__(self, name, pension1, pension2):
        super().__init__(name, pension1 + pension2, OldCouple.room_members)
        self.calculate_expenses(self.appliances)
