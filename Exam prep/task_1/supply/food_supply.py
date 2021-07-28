from task_1.supply.supply import Supply


class FoodSupply(Supply):
    needs_inc = 20

    def __init__(self):
        super().__init__(needs_increase=FoodSupply.needs_inc)

