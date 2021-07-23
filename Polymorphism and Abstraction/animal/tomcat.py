from animal.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")
        self.sound = "Hiss"
