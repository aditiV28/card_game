from constants import SUIT_VALUES, RANK_VALUES

class Card:
    #Initiliaze rank and suit
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit 
    
    #Conver the Card into a string
    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    #Python's magic methods useful to compare 2 cards
    def __lt__(self, other: 'Card') -> bool:
        if RANK_VALUES[self.rank] == RANK_VALUES[other.rank]:
            return SUIT_VALUES[self.suit] < SUIT_VALUES[other.suit]
        return RANK_VALUES[self.rank] < RANK_VALUES[other.rank]
    
    def __gt__(self, other: 'Card') -> bool:
        return other < self
    
    def __eq__(self, other: 'Card') -> bool:
        return self.rank == other.rank and self.suit == other.suit