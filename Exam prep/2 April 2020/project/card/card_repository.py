class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        if card in self.cards:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        result = [c for c in self.cards if c.name == card][0]
        self.cards.remove(result)
        self.count -= 1

    def find(self, name):
        return [c for c in self.cards if c.name == name][0]
