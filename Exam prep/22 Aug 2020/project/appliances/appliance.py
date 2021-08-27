class Appliance:
    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        month = 30
        return self.cost * month
