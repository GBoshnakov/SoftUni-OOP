from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = ""

    def make_sound(self):
        return self.sound

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"
