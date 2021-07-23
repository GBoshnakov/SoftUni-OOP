from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        if distance * self.fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= distance * self.fuel_consumption

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    extra_consumption = 0.9

    def drive(self, distance):
        if distance * (self.fuel_consumption + Car.extra_consumption) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.extra_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    extra_consumption = 1.6

    def drive(self, distance):
        if distance * (self.fuel_consumption + Truck.extra_consumption) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Truck.extra_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
