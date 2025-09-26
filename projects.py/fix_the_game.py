# BG 1st Fixing codes.

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    #run time error the attempts was = 0 so I fixed it to 10
    attempts = 10
    game_over = False
    while not game_over:
        # logic error there is no int so I put an int
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        
        if guess < number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        # The sygn was a logic error by having the sign flipped the opposite way
        elif guess > number_to_guess:
            print("Too low! Try again.")
        #this is a logic error elif is "if" is this then this is True or false

        #the sign was wrong
        elif guess == number_to_guess:
            print("Too High! Try again.")  
        continue
    print("Game Over. Thanks for playing!")
start_game()


import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    #Logic error attemts = 0 there must be more to work so its 10
    attempts = 10
    game_over = False
    while not game_over:
        #logic error no int for int(input("enter a number"))
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        continue
    print("Game Over. Thanks for playing!")
start_game()