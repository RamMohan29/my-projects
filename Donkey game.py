from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck = []

class Card(IntEnum):
    Two = 2
    Three = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    

class Suit(Enum):
    CLUBS = "clubs" 
    DIAMONDS = "diamonds" 
    HEARTS = "hearts" 
    SPADES = "spades"



class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

create_deck()
partial_deck = list(full_deck)
test_card = draw_card(partial_deck)     
print("You drew a:" ,test_card.card, test_card.suit)



def draw_card(deck):
    rand_card =randint(0, len(deck) -1) 
    return deck.pop(rand_card)





