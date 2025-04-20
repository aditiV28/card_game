SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
SUIT_VALUES = {'♠': 4, '♥': 3, '♦': 2, '♣': 1}
RANK_VALUES = {rank: index for index, rank in enumerate(RANKS, start=2)}
STARTING_BALANCE = 100