#BG 1st fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")
        #needed only numbers logic error otherwise the code will not work if there is a character that is not a number
        if guess.isalpha():
            print("Needs to be a number")
        if guess.isdigit():
            guess1 = int(guess)

            #needed an attempt indicator add on logic error otherwise it would just let you guess until you make it
            attempts = attempts + 1
            #Logic error the >= needs to be after guess corectly otherwise the last guess will never be seen as correct
            if guess1 == number_to_guess:
                print("Congratulations! You've guessed the number!")
                game_over = True
            elif attempts >= max_attempts:
                print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
                game_over = True  
            elif guess1 > number_to_guess:
                print("Too high! Try again.")
            elif guess1 < number_to_guess:
                print("Too low! Try again.")
        #continue not nessesary at end of
    print("Game Over. Thanks for playing!")
start_game()