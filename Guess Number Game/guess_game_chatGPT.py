import random

def guess_game():
    # Greet the player and get their name
    print("🎮 Welcome to the Guess Game!")
    player_name = input("What's your name? ").capitalize()
    print(f"Hello, {player_name}! Let's play a guessing game 😄")
    
    # Initialize scores
    best_score = 0  # highest score across games

    # Game loop (to allow replaying)
    while True:
        # Start each game with a full score
        score = 10
        # Generate a random number between 1 and 10
        secret_number = random.randint(1, 10)
        print("\nI've chosen a number between 1 and 10. Can you guess it?")
        
        # Flag to track win status
        player_won = False

        # Player can keep guessing until they get it right
        while not player_won:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("❌ Please enter a valid number!")
                continue
            
            # Check if guess is correct
            if guess == secret_number:
                print(f"🎉 Congratulations {player_name}! You guessed it right.")
                print(f"🏆 Your score this round: {score}")
                
                # Update best score if this one is higher
                if score > best_score:
                    best_score = score
                    print(f"🔥 New high score: {best_score}!")
                else:
                    print(f"Your highest score so far is: {best_score}")
                
                player_won = True  # exit inner loop
            else:
                # Deduct a point for wrong guess
                score -= 1
                if score <= 0:
                    print("😢 You're out of points! Better luck next time.")
                    break
                elif guess < secret_number:
                    print("📉 Too low! Try again.")
                else:
                    print("📈 Too high! Try again.")
                print(f"Current score: {score}")
        
        # Ask if the player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ("yes", "y"):
            print(f"\n✨ Thanks for playing, {player_name}!")
            print(f"Your highest score was: {best_score}")
            print("Goodbye 👋")
            break


# Run the game
if __name__ == "__main__":
    guess_game()
