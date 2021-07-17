from wild_cat_zoo.animal import Animal


class Tiger(Animal):
    money_for_care = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Tiger.money_for_care)