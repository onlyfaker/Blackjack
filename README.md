# Blackjack Game

A command-line implementation of the classic casino card game Blackjack, written in Python.

## 🃏 Game Overview

This Blackjack game follows standard casino rules where players try to get as close to 21 without going over. The dealer (computer) must hit until reaching at least 17 points.

### Features:
- Single-player gameplay against a computer dealer
- Player options to hit (draw a card) or stand (end turn)
- Ace handling (11 or 1) for both player and dealer hands
- Game continually prompts for new rounds

## 📋 Game Rules

- The goal is to have a hand value closer to 21 than the dealer without exceeding 21
- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10 points
- Aces are worth 11 points, but become 1 point if the hand would otherwise exceed 21
- Players are initially dealt 2 cards, while the dealer shows only 1 card
- Players can "hit" to receive additional cards or "stand" to end their turn
- The dealer must hit until reaching a minimum of 17 points
- Blackjack (21 points with first two cards) is an automatic win

## 🎮 How to Play

1. Run the game in your terminal
2. Choose whether to play a game by typing 'y' (yes) or 'n' (no)
3. If you choose to play:
   - You'll be dealt 2 cards, and the dealer will receive 1 card
   - Choose to hit ('h') to receive another card or stand ('s') to keep your current hand
   - If you go over 21, you lose automatically (bust)
   - After you stand, the dealer plays according to fixed rules
   - The hand values are compared to determine a winner

## 💻 Technical Implementation

### Dependencies
- Python 3.x
- `art.py` module (contains `LOGO` and `RULES` constants for display)
- `random` module (for card selection)

### Key Functions
- `generateCard()`: Randomly selects a card from the deck
- `handle_ace()`: Handles ace conversion from 11 to 1 when necessary
- `computerTurn()`: Manages the dealer's automated play

### Code Structure
The game uses a main loop structure with nested loops for:
1. Game continuity (play multiple rounds)
2. Input validation (ensuring valid player choices)
3. Player turn management (hit or stand decisions)

## 🚀 Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/blackjack-game.git
```

2. Navigate to the project directory:
```
cd blackjack-game
```

3. Ensure you have the `art.py` file with the required constants

4. Run the game:
```
python blackjack.py
```

## 🛠️ Customization Options

The game can be extended with:
- Betting functionality (commented in the code as a potential feature)
- Multiplayer support
- Split pairs
- Double down options
- Insurance bets

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
