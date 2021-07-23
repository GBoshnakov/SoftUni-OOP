class Equipment:
    _id = 0

    def __init__(self, name):
        Equipment._id += 1
        self.name = name
        self.id = Equipment._id

    @staticmethod
    def get_next_id():
        return Equipment._id + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
