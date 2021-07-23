from wild_farm.animals.animal import Mammal
from wild_farm.animals.birds import Owl
from wild_farm.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    weight_gainer = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if type(food) != Vegetable and type(food) != Fruit:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * Mouse.weight_gainer
        self.food_eaten += food.quantity


class Dog(Mammal):
    weight_gainer = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if type(food) != Meat:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * Dog.weight_gainer
        self.food_eaten += food.quantity


class Cat(Mammal):
    weight_gainer = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if type(food) != Meat and type(food) != Vegetable:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * Cat.weight_gainer
        self.food_eaten += food.quantity


class Tiger(Mammal):
    weight_gainer = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food) != Meat:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * Tiger.weight_gainer
        self.food_eaten += food.quantity


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
