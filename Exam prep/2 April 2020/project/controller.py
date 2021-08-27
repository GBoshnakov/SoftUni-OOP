from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type_p, username):
        if type_p == "Beginner":
            self.player_repository.add(Beginner(username))
        elif type_p == "Advanced":
            self.player_repository.add(Advanced(username))
        return f"Successfully added player of type {type_p} with username: {username}"

    def add_card(self, type_c, name):
        if type_c == "Magic":
            self.card_repository.add(MagicCard(name))
        elif type_c == "Trap":
            self.card_repository.add(TrapCard(name))
        return f"Successfully added card of type {type_c}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField().fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for p in self.player_repository.players:
            result += f"Username: {p.username} - Health: {p.health} - Cards {p.card_repository.count}\n"
            for c in p.card_repository.cards:
                result += f"### Card: {c.name} - Damage: {c.damage_points}\n"
        return result
