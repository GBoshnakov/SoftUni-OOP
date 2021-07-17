from wild_cat_zoo.caretaker import Caretaker
from wild_cat_zoo.cheetah import Cheetah
from wild_cat_zoo.keeper import Keeper
from wild_cat_zoo.lion import Lion
from wild_cat_zoo.tiger import Tiger
from wild_cat_zoo.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        # total_sum_to_pay = 0
        # for worker in self.workers:
        #     total_sum_to_pay += worker.salary
        total_sum_to_pay = sum(map(lambda worker: worker.salary, self.workers))

        if total_sum_to_pay <= self.__budget:
            self.__budget -= total_sum_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum_to_tend = 0
        for animal in self.animals:
            total_sum_to_tend += animal.money_for_care
        if total_sum_to_tend <= self.__budget:
            self.__budget -= total_sum_to_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(el) for el in self.animals if type(el) == Lion]
        tigers = [repr(el) for el in self.animals if type(el) == Tiger]
        cheetahs = [repr(el) for el in self.animals if type(el) == Cheetah]

        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join(lions) + "\n"

        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join(tigers) + "\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(cheetahs)

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(el) for el in self.workers if type(el) == Keeper]
        caretakers = [repr(el) for el in self.workers if type(el) == Caretaker]
        vets = [repr(el) for el in self.workers if type(el) == Vet]

        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join(keepers) + "\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join(caretakers) + "\n"

        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join(vets)

        return result


