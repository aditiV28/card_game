class Player:
    #Initialise player
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance

    #Place a bet
    def place_bet(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    #Win a bet
    def win_bet(self, amount: int) -> None:
        self.balance += amount * 2

    #Reset balance
    def reset_balance(self) -> None:
        self.balance = 100
