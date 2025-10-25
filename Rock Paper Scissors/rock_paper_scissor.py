import random

# Start Game
print("Welcome to Rock, Paper, and Scissors game!")

options = ["rock", "paper", "scissors"]

# Ask the player what your choice?
player_choice = input("Choice your game (Rock, Paper, and Scissors): ").strip().lower()
# make PC choice randomly
pc_choice = random.choice(options)

print(f"Your choice: {player_choice}\nComputer choice: {pc_choice}")

if player_choice == pc_choice:
    print("Oh! it's a tie")
  
elif (player_choice == "rock" and pc_choice == "scissors") or (player_choice == "paper" and pc_choice == "rock") or (player_choice == "scissors" and pc_choice == "paper"):
    print("Congrats! you won.")

else:
    print("You lose, Conputer won.")