from project.rooms.room import Room


class AloneOld(Room):
    room_members = 1
    room_cost = 10

    def __init__(self, name, pension):
        super().__init__(name, pension, AloneOld.room_members)
