# 🪨 Rock, Paper, Scissors Game

A simple Python command-line game that lets you play **Rock, Paper, Scissors** against the computer.

---

## 🎮 How It Works

1. The program greets you and asks you to choose one of the following:
   - **Rock**
   - **Paper**
   - **Scissors**
2. The computer randomly selects its choice.
3. Both choices are displayed, and the winner is decided based on the classic game rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same choice → It's a tie

---

## 🧠 Game Logic

```python
if player_choice == pc_choice:
    print("Oh! it's a tie")

elif (player_choice == "rock" and pc_choice == "scissors") or \
     (player_choice == "paper" and pc_choice == "rock") or \
     (player_choice == "scissors" and pc_choice == "paper"):
    print("Congrats! you won.")
else:
    print("You lose, Computer won.")
```

## ⚙️ Requirements

- Python 3.x
- No external libraries required (uses only the built-in random module)

## ▶️ How to Run

1. Clone this repository

   - git clone https://github.com/baselelsrogy/rock-paper-scissors.git
   - cd rock-paper-scissors

2. Run the script
   - python main.py
