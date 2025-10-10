#BG 1st password streanth

user_score = 0

while True:
    user_pass = input("enter a password")

    #user pass = upper
    if user_pass.isupper():
        user_score = user_score + 1
    #user pass = secial charecter
    #user pass = lower
    if user_pass is user_pass.islower():
        user_score = user_score + 1


    #user pass = number
    if user_pass.isdigit():
        user_score = user_score + 1

    #user pass = lenghth >= 8
    if len(user_pass >= 8):
        user_score = user_score + 1
    
    print(user_score)