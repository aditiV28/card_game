from cards.deck import Deck
from players.player import Player
from utils import get_valid_bet, get_valid_input

class HiLoCardGame:
    #Initialise starting balance, player and deck
    def __init__(self, player_name: str) -> None:
        from constants import STARTING_BALANCE
        self.player = Player(player_name, STARTING_BALANCE)
        self.deck = Deck()

    #Game logic
    def play_game(self) -> None:
        print(f"\nYour current balance is: ${self.player.balance}")
        print(f"\nCards remaining in the deck: {len(self.deck.cards)}")

        if len(self.deck.cards) < 2:
            print("\nNot enough cards to continue. Shuffling a new deck.")
            self.deck = Deck()
        
        first_card = self.deck.draw_card()
        print(f"\nFirst card: {first_card}")

        guess = get_valid_input("\nWill the next card be higher or lower? (h/l): ", ['h','l'])
        bet = get_valid_bet(self.player.balance)
        self.player.place_bet(bet)

        second_card = self.deck.draw_card()
        print(f"\nSecond card: {second_card}")

        if (second_card > first_card and guess == 'h') or (second_card < first_card and guess == 'l'):
            print("\n------------------------ You win!! ------------------------")
            self.player.win_bet(bet)
        else:
            print("\n------------------------ You lose!! ------------------------")

    #Start a new round
    def start(self) -> None:
        while True:
            while self.player.balance > 0:
                self.play_game()
                play_again = get_valid_input("\nDo you want to play again? (y/n)", ['y', 'n'])
                if play_again == 'n':
                    print(f"\nThanks for playing {self.player.name}! Your final balance is: ${self.player.balance}. \nSee you again!!")
                    return

            print("\nOh nooo! You are out of balance!! You cannot wager a balance of 0...")
            restart = get_valid_input("\nDo you want to restart the game? (y/n)", ['y', 'n'])
            if restart == 'y':
                self.player.reset_balance()
                self.deck = Deck()
                print("\n**************************** Game restarting... ****************************")
            else:
                print(f"\nThanks for playing {self.player.name}! Your final balance is: ${self.player.balance}. \nSee you again!!")
                return
