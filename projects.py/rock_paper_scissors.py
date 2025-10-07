#BG 1st rock paper scissors

import random

rock = """
    _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
    """

paper = """
    _______
---'   ____)____
          ______)
         _______)
         _______)
---.__________)
    """

scissors = """
    _______
---'   ____)____
          ______)
      __________)
        (____)
  ---.__(___)
    """



game = [rock, paper, scissors, quit]
game_over = False
user_score = 0
cp_score = 0

print("Wellcome to the rock paper sissors game info will follow")
while game_over == False and user_score <11 and cp_score < 11:
        print(user_score)
        print(cp_score)
        user_choice = int(input("0 for Rock, 1 for Paper, 2 for Scissors or 3 for quit.\n"))

        if not (0 <= user_choice <= 4):
            print("Invalid input. Please choose 0, 1, 2, or 3.")
            continue

        print("You chose:")
        print(game[user_choice])
        if user_choice == 3:
            print("Quiting...\n Good bye")
            break
        

        if user_choice == "3":
            game_over = True

        cp_choice = random.randint(0, 2)
        print("computer chose:")
        print(game[cp_choice])

        if user_choice == cp_choice:
            print("It's a draw!")
        elif (user_choice == 0 and cp_choice == 2) or \
            (user_choice == 1 and cp_choice == 0) or \
            (user_choice == 2 and cp_choice == 1):
            print("You win!")
            user_score = user_score + 1
        else:
            print("You lose!")
            cp_score = cp_score + 1
