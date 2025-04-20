# Hi-Lo Card Game (Terminal Edition)

A terminal-based Hi-Lo card game built in Python, following modular design, good software design principles such as encapsulation, separation of concerns, and extensibility. This game uses a 52-card poker deck(no jokers) and allows players to bet credits on whether the next card will be higher or lower in rank.

---

## Features

- Standard 52-card deck (no jokers)
- Suits ranked: ♠ > ♥ > ♦ > ♣
- Ranks: 2 < 3 < ... < 10 < J < Q < K < A
- Player wallet with betting system
- Encapsulation: Used classes to encapsulate data and logic.
- Separation of Concerns: Logic is been separated into classes, game logic, user input, helper functions (utils.py) and constants.
- Extensibility: More features can be easily added.
- Typing & PEP8: Type hints, adherence to naming conventions and spacing are followed throughout the code.
- Error Handling: Graceful handling of bad inputs and empty decks.
- Clean code : using PEP8 & static analysis with Ruff

---

## Game Rules

1. Player starts with 100 credits.
2. One card is drawn and shown to the player.
3. Player guesses whether the next card will be **higher** or **lower**.
4. Player places a bet.
5. The next card is drawn.
6. If the guess is correct, the player wins and the wallet is added with the number of credits won
7. If incorrect, the bet is lost and the wallet is subtracted with the number of credits lost
8. Repeat for as many rounds as desired, or until the wallet reaches 0, or until player doesn't want to continue
9. If wallet reaches 0, allow the player to restart

---

## Project Structure

```
card_game/
├── Dockerfile
├── main.py
├── requirements.txt
├── utils.py
├── constants.py
├── cards/
│   ├── __init__.py
│   ├── card.py
│   └── deck.py
├── games/
│   ├── __init__.py
│   └── hi_lo_card_game.py
├── players/
│   ├── __init__.py
│   └── player.py

```

- constants.py: File containing constants used across the application
- card.py: Contains the Card class and methods to initialise the card object and to compare two cards with respect to both rank and suit
- deck.py: Contains the Deck class and methods to initialise the deck object, randomly shuffle the deck and draw a card from the deck
- player.py: Contains the Player class and methods to initialise the player object, placing a bet and winning a bet
- hi_lo_card_game.py: Contains the HiLoCardGame class and methods to initialise the game for the player, game logic and  starting a new round
- utils.py: Contains helper functions to validate command line inputs and bet amount
- main.py: Entry point of the application
- Dockerfile: Contains the docker image, path to working directory inside the container, commands to install dependecies and to run the application
- requirements.txt: Contains details about the versions of any installed dependencies

---

## Versions used
- Python 3.13.3
- pip (24.0)
- ruff 0.11.6

## Setup (Local)

1. **Clone the repository:**
```bash
    git clone https://github.com/aditiV28/hi_lo_card_game.git
    cd "folder_name"
```

2. **Run the game:**

   ```bash
   python main.py
   ```

## Running with Docker

You can also run the game using Docker.

## Build the Docker Image

- Start the docker engine on your system using application like Docker Desktop

```bash
docker build -t hi_lo_game .
```

## Run the Game Interactively

```bash
docker run -it hi_lo_game
```

> The `-it` flag ensures you can interact with the game through the terminal.

---

### Run Ruff:

```bash
ruff check .
```

---
   
