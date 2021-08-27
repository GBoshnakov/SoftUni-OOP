class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses + room.room_cost
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            total_to_pay = room.expenses + room.room_cost
            if room.budget >= total_to_pay:
                room.budget -= total_to_pay
                result += f"{room.family_name} paid {total_to_pay:.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                self.rooms.remove(room)
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
        return result.strip("\n")

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                c = 1
                for child in room.children:
                    result += f"--- Child {c} monthly cost: {child.get_monthly_expense():.2f}$\n"
                    c += 1
            if room.appliances:
                total_expenses = 0
                for app in room.appliances:
                    total_expenses += app.get_monthly_expense()
                result += f"--- Appliances monthly cost: {total_expenses:.2f}$\n"
        return result
