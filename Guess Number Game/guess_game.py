import random

attempts_list = []
attempts = 0
rand_number = random.randint(1, 10)

def diaplay_score():
    if not attempts_list:
        print("You don't have a score lets play game!")
    else:
        print(f"Your current high score {min(attempts_list)} attempts.")
    


player_name = input("Welcome to Guess Number Game!\nWhat's your name?: ").capitalize().strip()
wanna_play = input(f"Hi {player_name}, would you like to try play?\nEnter(Yes/No): ").lower()

if wanna_play == "no":
    print("That's nice, have a good day.")
    exit()
else:
    diaplay_score()

while wanna_play == "yes":
    try:
        guess = int(input("Pick a number between 1 to 10: "))
        if guess < 1 or guess > 10:
            raise ValueError("please guess a number between range game!")
        
        attempts += 1

        if guess == rand_number:
            
            print(f"That's cool you got it!\nYour attempts is {attempts}")
            
            wanna_play = input("Would you like to play again?\nEnter (Yes/No): ").lower()

            attempts_list.append(attempts)
            
            if wanna_play == "no":
                diaplay_score()
            else:
                attempts = 0
                rand_number = random.randint(1, 10)
                diaplay_score()
                continue

        elif guess > rand_number:
            print("It's a high guess number! try again")
        else:
            print("It's a low guess number! try again")
                
        if guess > rand_number:
            print("It's higher")
            
        
    except ValueError as err:
        print(err)
        
    
