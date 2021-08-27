from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_members = 1
    room_cost = 10
    appliances = [TV()]

    def __init__(self, name, salary):
        super().__init__(name, salary, AloneYoung.room_members)
        self.calculate_expenses(AloneYoung.appliances)
