#BG 1st rock paper sissors

import random
user_score = 0
cp_score = 0

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""

sissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

while True:
    print(user_score)
    print(cp_score)
    if user_score <10 or cp_score <10:
        user = input("enter rock (r) paper (p) or sissors (s)")
        
    if user == "rock" or "r":
            print(rock)

    if user == "paper" or "p":
            print(paper)

    if user == "sissors" or "s":
            print(sissors)
    else:
            if user != "rock" or user != "r"\
            or user != "paper" or user != "p"\
            or user != "sissors" or user != "s":
                print("try againg")

    cp = random.randint(1,4)
    if cp == 1: 
            cp = rock
            print("rock")
            
    if cp == 2:
            cp = paper
            print("paper")
             
    if cp == 3:
            cp =sissors
            print("sissors")
             
        #tie
    if user == rock and cp == rock\
        or user == paper and cp == paper\
        or user == sissors and cp == sissors:
            print("tie")
             
        #user wins
    if user == rock and cp == sissors\
        or user == paper and cp == rock\
        or user == sissors and cp == paper:
            print("Player wins")
            user_score += 1
            continue
        #cp wins
    if cp == rock and user == sissors\
        or cp == paper and user == rock\
        or cp == sissors and user == paper:
            print("Computer wins")
            cp_score += 1
            continue
    else:
        print(cp_score)
        print(user_score)