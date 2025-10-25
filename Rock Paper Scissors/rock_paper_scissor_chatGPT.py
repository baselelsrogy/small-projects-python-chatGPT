import random

def get_player_choice(options):
    """Get and validate player's choice."""
    while True:
        choice = input(f"Choose your move ({', '.join(options)}): ").strip().lower()
        if choice in options:
            return choice
        print("❌ Invalid choice. Please try again.")

def get_winner(player, computer):
    """Determine the winner."""
    if player == computer:
        return "tie"
    
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    return "player" if wins[player] == computer else "computer"

def play_round():
    """Play one round of Rock, Paper, Scissors."""
    options = ["rock", "paper", "scissors"]

    print("🪨📄✂️  Welcome to Rock, Paper, Scissors!")
    player_choice = get_player_choice(options)
    computer_choice = random.choice(options)

    print(f"\n🧍 You chose: {player_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    winner = get_winner(player_choice, computer_choice)
    
    if winner == "tie":
        print("🤝 It's a tie!")
    elif winner == "player":
        print("🎉 You won!")
    else:
        print("💀 You lose. Computer wins.")

if __name__ == "__main__":
    play_round()
