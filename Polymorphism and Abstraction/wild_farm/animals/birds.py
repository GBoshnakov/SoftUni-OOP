from wild_farm.animals.animal import Bird
from wild_farm.food import Meat


class Hen(Bird):
    weight_gainer = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * Hen.weight_gainer
        self.food_eaten += food.quantity


class Owl(Bird):
    weight_gainer = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if type(food) != Meat:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * Owl.weight_gainer
        self.food_eaten += food.quantity

