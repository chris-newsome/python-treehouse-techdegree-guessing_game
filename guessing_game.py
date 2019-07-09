import random

import os

# Variable for high score set to empty list
high_score = []

# Function that uses the OS module to clear the screen when the user wants to play again
def clear_screen():
    
    os.system("cls" if os.name == "nt" else "clear")

# Function to display a welcome message for the game    
def welcome_message():
    
    print("""
    ====================================
    Welcome to the Number Guessing Game!
    ====================================
    
    Developed by: Christopher Newsome

    Here are the rules:
    
    Choose a number between 1 and 10.

    Try to guess the number in as few guesses as possible.
    
    Have fun!
    """)

# Function that stores a random number between 1 and 10   
def generate_secret_number():
    
    secret_number = random.randint(1, 10)
    
    return secret_number

# Function that asks the user to pick a number
def ask_user_input(message = "\nPick a number: "):
    
    while True:
        
        try:
            
            guess = int(input(message))
            
            return guess
            
        except UnboundLocalError and ValueError:
            
            print("\nuh oh! Please enter a valid number between 1 and 10 and try again!")
            
            continue

# Function that loops through guesses until guessed correctly
def guess_game(guess, secret_number):
    
    if 1 <= guess < secret_number:
        
        return "\nToo low! The number is greater than " + str(guess)
    
    elif 10 >= guess > secret_number:
        
        return "\nToo high! The number is less than " + str(guess)
    
    elif guess > 10:
        
        return str(guess) + " is not correct. The number must be between 1 and 10."
    
    elif guess < 1:
        
        return str(guess) + " is not correct. The number must be between 1 and 10."
    
    elif secret_number == guess:
        
        return "You got it!"

# Function that asks if the user would like to play again    
def restart_game():
    
    restart = (input("\nWould you like to play again? [y]es or [n]o? "))
    
    if restart.lower().strip() == "n":
        
        print("\nThank you for playing! Hope to see you again soon!")
        
        exit()
        
    if restart.lower().strip() == "y":
        
        return False

# Function that starts the game
def start_game():
    
    # Variable set to False at start of game
    user_congratulated = False

    # Variable allows the game to begin    
    start = True
    
    # If either statement is true, it loops until correct guess is correct
    # Sets the high score and displays it to the user at next game play
    while user_congratulated or start:

        guess_count = 0
        
        welcome_message()
                      
        secret_number = generate_secret_number()
        
        guess = ask_user_input()
        
        guess_count += 1
        
        message = guess_game(guess, secret_number)
        
        while guess != secret_number:
            
            print(message)
            
            guess = ask_user_input("\nTry again and pick a new number: ")
            
            guess_count += 1
            
            message = guess_game(guess, secret_number)
        
        print()
        
        print(message, f"You guessed the secret number in {guess_count} try(s)!")
        
        high_score.append(guess_count)
            
        high_score.sort()
        
        if restart_game() == False:
            
            clear_screen()
                
            print("\n    *** The current high score is {} ***".format(high_score[0]))
            
            start_game()
        
        user_congratulated = True

if __name__ == '__main__':
    start_game()