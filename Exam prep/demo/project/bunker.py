class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [obj for obj in self.supplies if type(obj).__name__ == "FoodSupply"]
        if not result:
            raise IndexError("There are no food supplies left!")
        return result

    @property
    def water(self):
        result = [obj for obj in self.supplies if type(obj).__name__ == "WaterSupply"]
        if not result:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = [obj for obj in self.medicine if type(obj).__name__ == "Painkiller"]
        if not result:
            raise IndexError("There are no painkillers left!")
        return result

    @property
    def salves(self):
        result = [obj for obj in self.medicine if type(obj).__name__ == "Salve"]
        if not result:
            raise IndexError("There are no salves left!")
        return result

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            med = [obj for obj in self.medicine if type(obj).__name__ == medicine_type][-1]
            self.medicine.remove(med)
            med.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            supp = [obj for obj in self.supplies if type(obj).__name__ == sustenance_type][-1]
            self.supplies.remove(supp)
            supp.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")


