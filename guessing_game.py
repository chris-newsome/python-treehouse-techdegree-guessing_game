import random

import os

# Variable for high score set to empty list
high_score = []

def clear_screen():
    """Function that uses the OS module to clear the screen when the user wants to play again"""
    
    os.system("cls" if os.name == "nt" else "clear")
 
def welcome_message():
    """Function to display a welcome message for the game"""
    
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
 
def generate_secret_number():
    """Function that stores a random number between 1 and 10"""
    
    secret_number = random.randint(1, 10)
    
    return secret_number

def ask_user_input(message = "\nPick a number: "):
    """Function that asks the user to pick a number"""
    
    while True:
        
        try:
            
            guess = int(input(message))
            
            return guess
            
        except UnboundLocalError and ValueError:
            
            print("\nuh oh! Please enter a valid number between 1 and 10 and try again!")
            
            continue

def guess_game(guess, secret_number):
    """Function that loops through guesses until guessed correctly"""
    
    if 1 <= guess < secret_number:
        
        return "\nToo low! The number is greater than " + str(guess)
    
    elif 10 >= guess > secret_number:
        
        return "\nToo high! The number is less than " + str(guess)

    elif guess < 1 or guess > 10:

        return str(guess) + " is not correct. The number must be between 1 and 10."
    
    elif secret_number == guess:
        
        return "You got it!"
  
def restart_game():
    """Function that asks if the user would like to play again"""

    restart = (input("\nWould you like to play again? [y]es or [n]o? "))
    
    while restart.lower() != 'y' and restart.lower() != 'n':

        print("\nInvalid input. Please try again.")

        restart = input("\nWould you like to play again? (y/n) ")
        
    if restart.lower().strip() == "n":
        
        print("\nThank you for playing! Hope to see you again soon!")
        
        exit()
        
    elif restart.lower().strip() == "y":
        
        return False

def start_game():
    """Function that starts the game"""
    
    # Variable set to False at start of game
    user_congratulated = False

    # Variable allows the game to begin    
    start = True
    
    # If either statement is true, it loops until correct guess is correct
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
        
        # Sets the high score and displays it to the user at next game play
        high_score.append(guess_count)
            
        high_score.sort()

        if restart_game() == False:

            clear_screen()
                
            print(f"\n    *** The current high score is {high_score[0]} ***")
            
            start_game()
            
            user_congratulated = True

if __name__ == '__main__':
    start_game()