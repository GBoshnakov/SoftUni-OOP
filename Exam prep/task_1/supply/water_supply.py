from task_1.supply.supply import Supply


class WaterSupply(Supply):
    needs_inc = 40

    def __init__(self):
        super().__init__(needs_increase=WaterSupply.needs_inc)

