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

        cp = random.randint(1,3)
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
                cp_score += 1
                print("Computer wins")
                continue