import random


user_op1 = [X, O, cp_choose]

user_op2 = [first, second, cp_choose]

cp_op1 = [X, O]

cp_op2 = [first, second]

print("0 = Xs, 1 = Os, 2 = computer randomly choose")
user_input1 = (input(f"enter a number for being Xs, Os, or computer choose in {user_op1}"))
if user_input1 == user_input1.isdigit():
    for i in user_op1:
        if user_input1 == 0:
            user_game = list(user_op1[0])
            print(user_game)

        if user_input1 == 1:
            user_game = list(user_op1[1])
        if user_input1 == 2:
            cp = random.randint[cp_op1]
else:
    print("must be 0-3")