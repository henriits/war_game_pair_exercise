# check if card_deck argument cointains 52 cards aka dictionaries
# shuffle
# deal the cards
# clear the deck
import random

class PrepareDeck:
    def __init__(self, deck, no_of_players=2):
        self.deck = deck
        self.no_of_players = no_of_players
        self.players_hands = []

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        self.shuffle()
        card_deck_size = len(self.deck)
        for _ in range(self.no_of_players):
            hand = []
            for card in range(int(card_deck_size / self.no_of_players)):
                hand.append(self.deck[-1])
                # print(hand)
                self.deck.pop()
            self.players_hands.append(hand)
        return self.players_hands



