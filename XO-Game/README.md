# 🎮 XO Game (Tic-Tac-Toe)

A simple **Tic-Tac-Toe (X-O)** game built using **Python’s Tkinter GUI library**.  
This application allows **two players** to play the classic game on a 3x3 grid, keeps track of scores, and visually highlights the winner.

## 🧩 Features

- ✅ Two-player local gameplay (Player 1: X, Player 2: O)
- 🧠 Automatic turn switching between players
- 🏆 Score tracking for both players
- 🎨 Highlighted winning combinations
- 🔁 Restart button to start a new round
- 🕹️ Randomly selects which player starts first
- ⚡ Tie detection with unique background color for tied games

## 🖥️ How It Works

### 🎯 Gameplay Logic

1. The game starts with a random player (X or O).
2. Players take turns clicking on empty squares to place their mark.
3. After each move:
   - The program checks for a winner or tie using the `is_win()` function.
   - If a player wins, their score increases by 1, and the winning cells are highlighted.
   - If all cells are filled without a winner, it’s a tie.
4. The **Restart** button clears the board and starts a new game while keeping the scores.

---

## 🧠 Core Functions

| Function                 | Description                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| `next_turn(row, column)` | Handles player turns, updates the grid, checks for wins/ties, and switches turns.               |
| `is_win()`               | Checks all possible win conditions (rows, columns, diagonals) and highlights the winning cells. |
| `is_empty()`             | Determines if there are still empty squares left on the board.                                  |
| `restart_game()`         | Resets the board and starts a new round with a randomly chosen first player.                    |

---

## 🧱 GUI Structure

The interface is divided into multiple sections:

- **Title Frame:** Displays the game title.
- **Score Frame:** Shows Player 1 and Player 2’s current scores.
- **Game Grid (3x3):** The main Tic-Tac-Toe board where players click to play.
- **End Frame:** Includes the “Restart” button and the status message label.

---

## 🧰 Requirements

Make sure you have **Python 3.x** installed.

No external libraries are required — only the built-in `tkinter` and `random` modules are used.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   - git clone https://github.com/baselelsrogy/small-projects-python-chatGPT
   - cd XO-Game
   - python xo_game.py
   ```
