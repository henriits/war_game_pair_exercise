from card_deck_methods import PrepareDeck
from cards import CardDeck


#deck = PrepareDeck()

card = CardDeck()
new_cards = card.return_deck()

#print(new_cards)
#deck = PrepareDeck(new_cards)
no_of_players = 2

hand_size = len(new_cards)/no_of_players

"""player1 = PrepareDeck(new_cards, hand_size).deal()
player2 = PrepareDeck(new_cards, hand_size).deal()
print(player1)
print(player2)
print(len(player1))
print(len(player2))
"""


# player_a = Player(player_name="Adam", hand=players_deck[-1])

class Player:
    def __init__(self, player_name , hand):
        self.player_name = player_name
        self.hand = hand
        
    def show_card(self):
        last_card = self.hand[-1]
        print(f"{self.player_name} card : {last_card['name']}")
        
        
    def compare_hands(self,other_player):
        card_self = self.hand[-1]
        card_other = other_player.hand[-1]
        value_self = card_self["value"]
        value_other = card_other["value"]

        # compare

        if value_self > value_other:
            return self.player_name
        elif value_self < value_other:
            return other_player.player_name
        
player1 = Player(player_name="Bob", hand=PrepareDeck(new_cards, hand_size).deal())
player1.show_card()
player2 = Player(player_name="Tom", hand=PrepareDeck(new_cards, hand_size).deal())
player2.show_card()

winner = player1.compare_hands(player2)
print(f"winner is {winner}")