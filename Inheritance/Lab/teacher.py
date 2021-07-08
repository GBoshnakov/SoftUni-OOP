from Lab.person import Person
from Lab.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
