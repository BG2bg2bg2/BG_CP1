#BG 1st pass checker



#spectial charitcers
spectial_chericers = "!@#$%^&*()_+~`_+-={}|[];':<>?,./\\"
#numbers needed
num = '1234567890'

#for the pass to see if it has any of these
Upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"

#for the index latter on to see if pass has any of these
lower = "qwertyuioplkjhgfdsazxcvbnm"


#Loop until false
code = True
while code != False:
    #user score is cleared each run
    user_score = 0
    #enter a password
    user_pass = input("enter password ")
#check to see if there is numbers
    for i in user_pass:
        if i in num:
            #user score + 1 if true
            user_score = user_score + 1
            break
#check to see if there is lower letters
    for l in user_pass:
        if l in lower:
            #user score + 1 if ture
            user_score = user_score +1
            break
#check to see if there is Upber letters
    for a in user_pass:
        if a in Upper:
            user_score = user_score +1
            break
#check if there is special characters
    for b in user_pass:
        if b in spectial_chericers:
            user_score = user_score + 1
            break
#check to see if the password is 8 long
    if len(user_pass)>= 8:
        user_score += 1
    
    #if the score is equivelint to any of these it will tell if the pass is week-strong in streanth wise
    print(user_score)
    if user_score == 0:
        print("No blank password alowed")
    elif user_score <= 2:
        print("weak")
    elif user_score == 3:
        print("moderate")
    elif user_score == 4:
        print("strong")
    elif user_score == 5:
        print("Very strong")