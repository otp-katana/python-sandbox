# Rock-Paper-Scissors: Terminal Edition

An interactive, terminal-based Rock-Paper-Scissors game developed in Python, featuring rich ASCII art and mini terminal animations[cite: 11]. The project is designed with a modular architecture that isolates the core game logic from the user interface (UI)[cite: 11].

## Features

- **Modular Architecture:** The core game loop and score tracking are handled in `main.py`, while all graphical outputs, animations, and menus are called from the `utils.py` module[cite: 11].
- **Visual Feedback:** Includes characteristic ASCII illustrations (rock, paper, and scissors hands) and custom retro terminal screens for win, loss, and draw states[cite: 11, 12].
- **Dynamic Input Validation:** Invalid inputs (alphabetical or out-of-range) are caught using a `try/except ValueError` block. Instead of crashing the game, it displays a custom warning screen (`HatalıGiriş()`) and prompts the user to try again[cite: 10, 11, 12].
- **Cinematic Transitions:** Integrates faux system startup and shutdown (`ÇıkışAnimasyonu()`) effects that give the terminal screen a hacker/retro vibe[cite: 11, 12].
- **Scoring System:** Features a structured scoreboard that updates after every move, continuing until one of the players reaches 3 victories[cite: 10, 11, 12].

## Usage

Ensure that both `main.py` and `utils.py` are located in the same directory[cite: 11]. Run the following command in your terminal to start the game:

```bash
python main.py