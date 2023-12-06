# check if card_deck argument cointains 52 cards aka dictionaries
# shuffle
# deal the cards
# clear the deck
import random

class PrepareDeck:
    def __init__(self, deck, hand_size):
        self.deck = deck
        self.hand_size = hand_size
        self.players_hands = []

        
    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        self.shuffle()
        card_deck_size = len(self.deck)
        # for _ in range(self.no_of_players):
        hand = []
        for card in range(int(self.hand_size)):
            hand.append(self.deck[-1])
            # print(hand)
            self.deck.pop()
            # self.players_hands.append(hand)
        return hand



