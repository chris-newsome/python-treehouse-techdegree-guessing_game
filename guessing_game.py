import random

import os
    
high_score = []

def clear_screen():
    
    os.system("cls" if os.name == "nt" else "clear")
    
def welcome_message():
    
    print("""
    ====================================
    Welcome to the Number Guessing Game!
    ====================================
    
    Here are the rules:
    
    Choose a number between 1 and 10.

    Try to guess the number in as few guesses as possible.
    
    Have fun!
    """)
    
def generate_secret_number():
    
    # Stores random number
    secret_number = random.randint(1, 10)
    
    return secret_number

def username():
    
    player = input("Enter your name: ")
    
    return player

def ask_user_input(message = "Pick a number: "):
    
    while True:
        
        try:
            
            guess = int(input(message))
            
            return guess
            
        except UnboundLocalError and ValueError:
            
            print("\nuh oh! Please enter a valid number between 1 and 10 and try again!")
            
            continue

def guess_game(guess, secret_number):
    
    if 1 <= guess < secret_number:
        
        return "\nToo low! The number is greater than " + str(guess)
    
    elif 10 >= guess > secret_number:
        
        return "\n Too high! The number is less than " + str(guess)
    
    elif guess > 10:
        
        return str(guess) + " is not correct. The number must be between 1 and 10."
    
    elif guess < 1:
        
        return str(guess) + " is not correct. The number must be between 1 and 10."
    
    elif secret_number == guess:
        
        return "You got it!"
    
def restart_game():
    
    restart = (input("\nWould you like to play again? [y]es or [n]o? "))
    
    if restart.lower().strip() == "n":
        
        print("\nThank you for playing! Hope to see you again soon!")
        
        exit()
        
    if restart.lower().strip() == "y":
        
        return False

def start_game():
    
    user_congratulated = False
        
    start = True
    
    while user_congratulated or start:
        
        guess_count = 0
        
        welcome_message()
                      
        secret_number = generate_secret_number()
        
        print("For testing purposes, the secret number is {}\n".format(secret_number))
        
        guess = ask_user_input()
        
        guess_count += 1
        
        message = guess_game(guess, secret_number)
        
        while message != "You got it!":
            
            print(message)
            
            guess = ask_user_input("\nTry again and pick a new number: ")
            
            guess_count += 1
            
            message = guess_game(guess, secret_number)
        
        print()
        
        print(message, "You guessed the secret number in {} try(s)!".format(guess_count))
        
        high_score.append(guess_count)
            
        high_score.sort()

        if high_score[0] > guess_count:
            
            player = input("Enter your name: ")
            
            high_score.insert(0, guess_count)
            
            print("Congratulations {}! You have the new high score!".format(player))
        
        if restart_game() == False:
            
            clear_screen()
                
            print("\n      **The current high score is {}**".format(high_score[0]))
            
            start_game()
        
        user_congratulated = True

if __name__ == '__main__':
    print ("    ")  
    print ("Developed by: Christopher Newsome")   
    start_game()