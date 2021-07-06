class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self. hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        result = ""
        result += f"Name: {self.name}\n" \
                  f"Guild: {self.guild}\n" \
                  f"HP: {self.hp}\n" \
                  f"MP: {self.mp}\n"
        result += '\n'.join([f'==={key} - {val}' for key, val in self.skills.items()])
        return result


