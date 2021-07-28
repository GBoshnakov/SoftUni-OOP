from task_1.medicine.medicine import Medicine


class Salve(Medicine):
    health_inc = 50

    def __init__(self):
        super().__init__(health_increase=Salve.health_inc)


