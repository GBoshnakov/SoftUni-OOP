from wild_cat_zoo.animal import Animal


class Lion(Animal):
    money_for_care = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.money_for_care)