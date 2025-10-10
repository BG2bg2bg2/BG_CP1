user_input1 = ["X","O", "Cp"]
user_input2 = ["first", "second","Cp"]

print("0 = X, 1 = O, 2 = computer choose")
while True:
    user1 = input(f"enter a number 0-3 for {user_input1}")
    if user1 != user1.isdigit() or int(user1) > 3:
        print("must be a number")
        while True:
            if user1.isdigit() and int(user1) <=2:
                for i in user_input1:
                    user = user1 in user_input1