class CardDeck:
    def __init__(self):
        self.card_deck = []

    def __str__(self):
        return str(self.card_deck)

    @property
    def card_deck(self):
        return self._card_deck

    @card_deck.setter
    def card_deck(self, card_deck):
        self._card_deck = card_deck
        for _ in ["♥️", "♦️", "♠️", "♣️"]:
            print(_)
            self._card_deck += [{"name": _ + " A", "value": 14},
                {"name": _ + " K", "value": 13},
                {"name": _ + " Q", "value": 12},
                {"name": _ + " J", "value": 11},
                {"name": _ + " 10", "value": 10},
                {"name": _ + " 9", "value": 9},
                {"name": _ + " 8", "value": 8},
                {"name": _ + " 7", "value": 7},
                {"name": _ + " 6", "value": 6},
                {"name": _ + " 5", "value": 5},
                {"name": _ + " 4", "value": 4},
                {"name": _ + " 3", "value": 3},
                {"name": _ + " 2", "value": 2}]
            # print(self._card_deck)

cards = CardDeck()
print(cards)
