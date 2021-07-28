from task_1.medicine.medicine import Medicine


class Painkiller(Medicine):
    health_inc = 20

    def __init__(self):
        super().__init__(health_increase=Painkiller.health_inc)

