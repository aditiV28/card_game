#Accept valid inputs from command line
def get_valid_input(prompt: str, valid_choices: list[str]) -> str:
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"\nInvalid choice. Choose from {valid_choices}")

#Accept valid bet from command line
def get_valid_bet(balance: int) -> int:
    while True:
        try:
            bet = int(input(f"\nEnter your bet (Available balance is: ${balance}): "))
            if 0 < bet <= balance:
                return bet
            print("Invalid bet amount")
        except ValueError:
            print("\nEnter correct value for bet")

#Accept valid name from command line
def get_valid_name(name: str) -> str:
    try:
        name = name.strip()
        if not name or len(name) > 15 or not all(char.isalpha() or char.isspace() for char in name):
            return False
        else:
            return name
    except ValueError:
        print("\nInvalid name! Use only letters & spaces (max 15 characters). Please try again.")