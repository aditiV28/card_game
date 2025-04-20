import random
from typing import List
from constants import SUITS, RANKS 
from cards.card import Card 

class Deck:
    #Initialise the deck
    def __init__(self) -> None:
        self.cards: List[Card] = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        self.shuffle()

    #Randomly shuffle the deck
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    #Draw card from the deck
    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("The deck is empty")
        return self.cards.pop()
