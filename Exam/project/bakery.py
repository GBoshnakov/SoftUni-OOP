from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        result = [obj for obj in self.food_menu if obj.name == name]
        if result:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        result = [obj for obj in self.drinks_menu if obj.name == name]
        if result:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        result = [obj for obj in self.tables_repository if obj.table_number == table_number]
        if result:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if (not table.is_reserved) and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_name):
        table = [obj for obj in self.tables_repository if obj.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        in_menu = []
        not_in_menu = []
        for f in food_name:
            food = [obj for obj in self.food_menu if f == obj.name]
            if food:
                in_menu.append(food[0])
                table[0].food_orders.append(food[0])
            else:
                not_in_menu.append(f)
        info_food_in_menu = '\n'.join([repr(obj) for obj in table[0].food_orders])
        info_food_not_in_menu = '\n'.join(not_in_menu)
        result = f"Table {table_number} ordered:\n{info_food_in_menu}"
        result += f"\n{self.name} does not have in the menu:\n"
        result += info_food_not_in_menu
        return result

    def order_drink(self, table_number: int, *drinks_name):
        table = [obj for obj in self.tables_repository if obj.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        in_menu = []
        not_in_menu = []
        for d in drinks_name:
            drink = [obj for obj in self.drinks_menu if d == obj.name]
            if drink:
                in_menu.append(drink[0])
                table[0].drink_orders.append(drink[0])
            else:
                not_in_menu.append(d)
        info_drink_in_menu = '\n'.join([repr(obj) for obj in table[0].drink_orders])
        info_drink_not_in_menu = '\n'.join(not_in_menu)
        result = f"Table {table_number} ordered:\n{info_drink_in_menu}"
        result += f"\n{self.name} does not have in the menu:\n"
        result += info_drink_not_in_menu
        return result

    def leave_table(self, table_number: int):
        table = [obj for obj in self.tables_repository if obj.table_number == table_number][0]
        bill = table.get_bill()
        result = f"Table: {table.table_number}\nBill: {bill:.2f}"
        self.total_income += bill
        table.clear()
        return result

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info()+"\n"
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
