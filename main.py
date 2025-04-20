from games.hi_lo_card_game import HiLoCardGame
from utils import get_valid_name

def main() -> None:
    while True:
        raw_input = input("Enter your name:")
        name = get_valid_name(raw_input)
        if name:
            break
        print("\nInvalid name! Use only letters & spaces (max 15 characters). Please try again")

    print(f"\n**************************** Welcome {name} to Hi-Lo Card Game ****************************")
    game = HiLoCardGame(name)
    game.start()

if __name__ == "__main__":
    main()
